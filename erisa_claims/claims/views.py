from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Claim, ClaimDetail, ClaimNote, ClaimFlag
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def claims_list(request):
    page_number = int(request.GET.get('page', 1))
    search_text = request.GET.get('search_query', '')
    filter_option = request.GET.get('filter', '')
    claims_qs = Claim.objects.all().order_by('id')    
    if search_text:
        if filter_option == 'id':
            claims_qs = Claim.objects.filter(id__istartswith=search_text)
        elif filter_option == 'patient_name':
            claims_qs = Claim.objects.filter(patient_name__istartswith=search_text)
        elif filter_option == 'insurer_name':
            claims_qs = Claim.objects.filter(insurer_name__istartswith=search_text)
        else:
            claims_qs = Claim.objects.filter(
                Q(id__istartswith=search_text) | 
                Q(patient_name__istartswith=search_text) |
                Q(insurer_name__istartswith=search_text)
            )
    paginator = Paginator(claims_qs, 50)
    page_obj = paginator.get_page(page_number)

    # Render differently if HTMX request
    if request.headers.get('HX-Request'):
        # Return only the table body (partial)
        return render(request, "claim_table.html", {
            'claims': page_obj,
            'page_obj': page_obj
        })

    # Full page render
    return render(request, "claims.html", {
        'claims': page_obj,
        'page_obj': page_obj
    })

@login_required(login_url='/login/')
def claims_detail_modal(request, claim_id):
    claim_query = Claim.objects.get(id=claim_id)
    # Get the claim object
    claim = Claim.objects.get(id=claim_id)
    # Get all related claim details
    claim_detail = ClaimDetail.objects.filter(claim_id=claim_id).values(
        'denial_reason', 'cpt_codes'
    ).first()  # returns a dict or None
    claim_notes = claim.notes.all()
    claim_flags = claim.flags.all();
    cpt_codes = claim_detail['cpt_codes'].split(",")
    claim_combined_data = {
        "id": claim.id,
        "patient_name": claim.patient_name,
        "billed_amount": claim.billed_amount,
        "paid_amount": claim.paid_amount,
        "status": claim.status,
        "insurer_name": claim.insurer_name,
        "discharge_date": claim.discharge_date,
        "cpt_codes": cpt_codes,
        "denial_reason": claim_detail['denial_reason'],
        "claim_notes": claim_notes,
        "claim_flags": claim_flags,
    }
    return render(request, "claim_detail_modal.html", {'claim_detail' : claim_combined_data})

@login_required(login_url='/login/')
def claims_form_modal(request, claim_id, form_type):
    claim = get_object_or_404(Claim, id=claim_id)
    basic_claim_info = {
        "id": claim.id,
        "patient_name": claim.patient_name,
        "status": claim.status,
    }
    if form_type == 'note':
        return render(request, "claim_note.html", {"claim" : basic_claim_info})
    elif form_type == 'flag':
        return render(request, "claim_flag.html", {"claim" : basic_claim_info})
    else:
        return HttpResponse("Invalid form type", status=400)
    
@login_required(login_url='/login/')
def claims_create_note(request, claim_id):
    #print("Creating note...")
    if request.method == "POST":
        form_text = request.POST.get("form_text", "").strip()
        if form_text:  # only create if not empty
            claim = Claim.objects.get(id=claim_id)
            ClaimNote.objects.create(
                claim=claim,
                note_text=form_text,
                user_id=request.user  # pass the user instance
            )
        else:
            # Optional: return 400 Bad Request if text is empty
            return HttpResponse("Note text cannot be empty.", status=400)
    return HttpResponse(status=204)

@login_required(login_url='/login/')
def claims_create_flag(request, claim_id):
    #print("Creating flag...")
    if request.method == "POST":
        form_text = request.POST.get("form_text", "").strip()
        if form_text:  # only create if not empty
            claim = Claim.objects.get(id=claim_id)
            ClaimFlag.objects.create(
                claim=claim,
                flag_text=form_text,
                user_id=request.user  # pass the user instance
            )
        else:
            # Optional: return 400 Bad Request if text is empty
            return HttpResponse("Flag text cannot be empty.", status=400)
    return HttpResponse(status=204)

@login_required(login_url='/login/')
def claims_show_flags(request):
    page_number = int(request.GET.get('page', 1))
    search_text = request.GET.get('search_query', '')
    filter_option = request.GET.get('filter', '')

    # Start with claims that have at least one flag
    claims_qs = Claim.objects.filter(flags__isnull=False).distinct().order_by('id')

    # Apply search/filtering if needed
    if search_text:
        if filter_option == 'id':
            claims_qs = claims_qs.filter(id__istartswith=search_text)
        elif filter_option == 'patient_name':
            claims_qs = claims_qs.filter(patient_name__istartswith=search_text)
        elif filter_option == 'insurer_name':
            claims_qs = claims_qs.filter(insurer_name__istartswith=search_text)
        else:
            claims_qs = claims_qs.filter(
                Q(id__istartswith=search_text) |
                Q(patient_name__istartswith=search_text) |
                Q(insurer_name__istartswith=search_text)
            )

    # Paginate
    paginator = Paginator(claims_qs, 50)
    page_obj = paginator.get_page(page_number)

    # Render differently if HTMX request
    if request.headers.get('HX-Request'):
        return render(request, "claim_table.html", {
            'claims': page_obj,
            'page_obj': page_obj
        })

    # Full page render
    return render(request, "claim_flags.html", {
        'claims': page_obj,
        'page_obj': page_obj
    })