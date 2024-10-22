from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *

# Create your views here.
class RobochiyNavchalnuyPlanInline():
    form_class=RobochiyNavchalnuyPlanForm
    model=RobochiyNavchalnuyPlan
    template_name="robochiy_navchalnuy_plan/robochiy_navchalnuy_plan_create_or_update.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                elementRNPs = formset.save(commit=False)
                for elementRNP in elementRNPs:
                    elementRNP.robochiyNavchalnuyPlan = self.object
                    elementRNP.save()
                formset.save_m2m()
        return redirect('list_robochiy_navchalnuy_plans')
    

    def formset_elementRNPs_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        elementRNPs = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for elementRNP in elementRNPs:
            elementRNP.robochiyNavchalnuyPlan = self.object
            elementRNP.save()


class RobochiyNavchalnuyPlanCreate(RobochiyNavchalnuyPlanInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(RobochiyNavchalnuyPlanCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'elementrnp': ElementRNPFormSet(prefix='elementrnp'),
                
            }
        else:
            return {
                'elementrnp': ElementRNPFormSet(self.request.POST or None, self.request.FILES or None, prefix='elementrnp'),
                
            }


class RobochiyNavchalnuyPlanUpdate(RobochiyNavchalnuyPlanInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(RobochiyNavchalnuyPlanUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'elementrnp': ElementRNPFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='elementrnp'),
            
        }
    

class  RobochiyNavchalnuyPlanList ( ListView ): 
    model = RobochiyNavchalnuyPlan
    template_name = "robochiy_navchalnuy_plan/robochiy_navchalnuy_plan_list.html"
    context_object_name = "robochiy_navchalnuy_plans"



def delete_elementrnp(request, pk):
    try:
        elementrnp = ElementRNP.objects.get(id=pk)
    except ElementRNP.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('update_robochiy_navchalnuy_plan', pk=elementrnp.robochiyNavchalnuyPlan.id)

    elementrnp.delete()
    messages.success(
            request, 'ElementRNP deleted successfully'
            )
    return redirect('update_robochiy_navchalnuy_plan', pk=elementrnp.robochiyNavchalnuyPlan.id)