import json
import os
from django.core.management.base import BaseCommand, CommandError
from claims.models import Claim, ClaimDetail

class Command(BaseCommand):
    help = "Load claims and claim details from JSON files into the database"

    def add_arguments(self, parser):
        parser.add_argument("claim_list_path", type=str, help="Path to claim_list.json")
        parser.add_argument("claim_details_path", type=str, help="Path to claim_detail.json")

    def handle(self, *args, **options):
        # Store paths to .json files
        list_path: str = options["claim_list_path"]
        details_path: str = options["claim_details_path"]

        # Check if paths exist
        if os.path.exists(list_path) == False:
            raise CommandError(f"Claims list file not found: {list_path}")
        if os.path.exists(details_path) == False:
            raise CommandError(f"Claim details file not found: {details_path}")

        # Check if files are .json files
        if list_path.lower().endswith(".json") == False:
            raise CommandError(f"Claim list file is not a .json file: {list_path}")
        if details_path.lower().endswith(".json") == False:
            raise CommandError(f"Claim details file is not a .json file: {details_path}")
        
        # Load the .json files
        try:
            with open(list_path, 'r') as f:
                claim_list_data = json.load(f)
        except json.JSONDecodeError as e:
            raise CommandError(f"Invalid JSON in claim list file: {e}")

        try:
            with open(details_path, 'r') as f:
                claim_details_data = json.load(f)
        except json.JSONDecodeError as e:
            raise CommandError(f"Invalid JSON in claim details file: {e}")
        
        # Create/Update the SQLite database
        for record in claim_list_data:
            Claim.objects.update_or_create(
                id = record["id"],
                defaults = {
                    "patient_name": record["patient_name"],
                    "billed_amount": record["billed_amount"],
                    "paid_amount": record["paid_amount"],
                    "status": record["status"],
                    "insurer_name": record["insurer_name"],
                    "discharge_date": record["discharge_date"],
                }
            )
        for record in claim_details_data:
            ClaimDetail.objects.update_or_create(
                id = record["id"],
                defaults = {
                    "claim_id": record["claim_id"],
                    "denial_reason": record["denial_reason"],
                    "cpt_codes": record["cpt_codes"],
                }
            )