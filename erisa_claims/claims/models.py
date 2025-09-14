from django.db import models
from authentication.models import ERISA_User

# Claim from claim_list.json
class Claim(models.Model):
    id = models.BigIntegerField(primary_key=True)
    patient_name = models.CharField(max_length=200)
    billed_amount = models.DecimalField(max_digits=12, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=50)
    insurer_name = models.CharField(max_length=100)
    discharge_date = models.DateField()

    class Meta:
        db_table = "claims"

    def __str__(self):
        return f"{self.id} - {self.patient_name}"

# Claim from claim_detail.json
class ClaimDetail(models.Model):
    id = models.BigIntegerField(primary_key=True)
    claim = models.ForeignKey(Claim, to_field="id", on_delete=models.CASCADE, related_name="details") # matches the 'id' in claim_detail.json
    denial_reason = models.TextField(blank=True, null=True)
    cpt_codes = models.CharField(max_length=200, blank=True, null=True)  # store as a whole string
    
    class Meta:
        db_table = "claim_details"

    def __str__(self):
        return f"Detail {self.id} for Claim {self.claim.id}"
    
class ClaimNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    claim = models.ForeignKey(Claim, to_field="id", on_delete=models.CASCADE, related_name='notes') # claim.notes.all() will give all notes for the claim
    note_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        "authentication.ERISA_User",
        to_field='id',
        on_delete=models.CASCADE,
        related_name="claim_notes",
        null=False,
    )
    class Meta:
        db_table = "claim_notes"

class ClaimFlag(models.Model):
    id = models.BigAutoField(primary_key=True)
    claim = models.ForeignKey(Claim, to_field="id", on_delete=models.CASCADE, related_name="flags")  # claim.flags.all() gives all flags for a claim)
    flag_text = models.CharField(max_length=250)  # short description of the flag
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        "authentication.ERISA_User",
        to_field='id',
        on_delete=models.CASCADE,
        related_name="claim_flags",
        null=False,
    )

    class Meta:
        db_table = "claim_flags"