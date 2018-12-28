from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product, ProductVote, ProductArea
from django.http import HttpResponse
from django.contrib import messages
from .forms import NewProductForm, NewProductAreaForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def all_products(request):
    if request.is_ajax() and request.method == 'POST':

        current_user = request.user

        if ProductVote.objects.filter(
            user_id=current_user.id).filter(
                product=request.POST['vote_id']):

            return HttpResponse(0)

        product = Product.objects.filter(id=request.POST['vote_id'])

        ProductVote.objects.create(product=product[0], user_id=current_user.id)

        return HttpResponse(request.POST['vote_id'])

    else:
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})

@login_required
def new_product(request):
    new_product_form = NewProductForm()
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Feature/Issue created')
            return redirect('products')
        else:
            messages.add_message(
                request, messages.ERROR, form.errors)

    args = {'new_product_form': new_product_form}
    return render(request, 'new_product.html', args)


@login_required
def edit_product(request, id=None, template_name='edit_product.html'):
    if id:
        product = get_object_or_404(Product, id=id)

    new_product_form = NewProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product,
        id=id)

    if request.POST and new_product_form.has_changed():

        if new_product_form.is_valid():
            product.save()
            return redirect('products')

    elif request.POST:
        messages.add_message(
            request, messages.ERROR, 'No changes to save')

    args = {'new_product_form': new_product_form, 'id': id}
    return render(request, template_name, args)

# TODO: delete product only by owner


@login_required
def new_product_area(request):
    product_area_form = NewProductAreaForm()
    if request.method == 'POST':
        form = NewProductAreaForm(request.POST)
        if form.is_valid():
            # file is saved
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Product Area created')
        else:
            messages.add_message(
                request, messages.ERROR, form.errors)

    args = {'new_product_area_form': product_area_form}
    return render(request, 'new_product_area.html', args)


@login_required
def edit_product_area(request, id=None, template_name='edit_product_area.html'):
    if id:
        product_area = get_object_or_404(ProductArea, id=id)

    new_product_area_form = NewProductAreaForm(
        request.POST or None,
        instance=product_area)

    if request.POST and new_product_area_form.has_changed():

        if new_product_area_form.is_valid():
            product_area.save()
            return redirect('product_areas')

    elif request.POST:
        messages.add_message(
            request, messages.ERROR, 'No changes to save')

    args = {'new_product_area_form': new_product_area_form}
    return render(request, template_name, args)


@login_required
def delete_product_area(request, id=None, template_name='edit_product_area.html'):
    if id:
        product_area = get_object_or_404(ProductArea, id=id)

        if Product.objects.filter(product_area_id=id):
            print(product_area)
            messages.add_message(
                request, messages.ERROR, "{} Cannot be deleted, Please delete Feature/Issue instead".format(product_area))
        else:
            product_area.delete()

    else:
        messages.add_message(
            request,
            messages.ERROR, "{} Not Deleted".format(product_area))

    return redirect('product_areas')


def all_product_areas(request):
    product_areas = ProductArea.objects.all()
    return render(
        request, "product_areas.html", {"product_areas": product_areas})
