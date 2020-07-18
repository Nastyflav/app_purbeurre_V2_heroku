#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-28
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.shortcuts import redirect
from django.views.generic import ListView, DetailView

from .models import Product


class ProductSearchView(ListView):
    """
    Displays a list of products matching with the user query

    Arguments: ListView {class} -- generic listview

    Returns: products -- products matching with search query

    """

    model = Product
    paginate_by = 6
    template_name = 'search/search_results.html'

    def parser(self, input):
        """Clean the query from all the alphanum symbols"""
        self.input = str(input).casefold()  # converts into lower cases
        # with open("search/symbols.txt", "r",
        #           encoding="cp1252") as file:
        #     file = file.readlines()
        #     for symbol in file:
        #         symbol = symbol.replace("\n", "")
        #         self.input = self.input.replace(symbol, " ")

    def get(self, request, *args, **kwargs):
        """To redirect if the query is empty"""
        query = self.request.GET.get("query")
        if query:
            return super(ProductSearchView, self).get(request, *args, **kwargs)
        else:
            return redirect('index')

    def get_queryset(self):
        """Get the query and the products matching it"""
        query = self.request.GET.get("query")
        query = str(query).casefold()
        with open("search/symbols.txt", "r",
                  encoding="cp1252") as file:
            file = file.readlines()
            for symbol in file:
                symbol = symbol.replace("\n", "")
                query = query.replace(symbol, "")

        return Product.objects.filter(
            name__icontains=query).order_by('-nutriscore')

    def get_context_data(self, **kwargs):
        """Returns the context"""
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get("query")
        return context


class ProductDetailsView(DetailView):
    """Display the details of a choosen product"""
    model = Product
    template_name = "search/product_details.html"
