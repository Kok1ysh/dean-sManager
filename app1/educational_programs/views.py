from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import (
    CreateView, UpdateView
)
from .models import *
from .forms import *

# Create your views here.
class EducationalProgramsInline():
    form_class=EducationalProgramsForm
    model=EducationalPrograms
    template_name="educational_programs/educational_programs__create_or_update.html"

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
                komponentEducationalPrograms = formset.save(commit=False)
                for komponentEducationalProgram in komponentEducationalPrograms:
                    komponentEducationalProgram.educationalProgram = self.object
                    komponentEducationalProgram.save()
                formset.save_m2m()
        return redirect('list_educational_programs')
    

    def formset_komponent_educational_programs_valid(self, formset):
        """
        Hook for custom formset saving.Useful if you have multiple formsets
        """
        komponentEducationalPrograms = formset.save(commit=False)  # self.save_formset(formset, contact)
        # add this 2 lines, if you have can_delete=True parameter 
        # set in inlineformset_factory func
        for obj in formset.deleted_objects:
            obj.delete()
        for komponentEducationalProgram in komponentEducationalPrograms:
            komponentEducationalProgram.educationalProgram = self.object
            komponentEducationalProgram.save()


class EducationalProgramsCreate(EducationalProgramsInline, CreateView):

    def get_context_data(self, **kwargs):
        ctx = super(EducationalProgramsCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'komponenteducationalprograms': KomponentEducationalProgramsFormSet(prefix='komponenteducationalprograms'),
                
            }
        else:
            return {
                'komponenteducationalprograms': KomponentEducationalProgramsFormSet(self.request.POST or None, self.request.FILES or None, prefix='komponenteducationalprograms'),
                
            }


class EducationalProgramsUpdate(EducationalProgramsInline, UpdateView):

    def get_context_data(self, **kwargs):
        ctx = super(EducationalProgramsUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'komponenteducationalprograms': KomponentEducationalProgramsFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object, prefix='komponenteducationalprograms'),
            
        }
    

class  EducationalProgramsList ( ListView ): 
    model = EducationalPrograms 
    template_name = "educational_programs/educational_programs_list.html"
    context_object_name = "educational_programs"



def delete_komponent_educational_programs(request, pk):
    try:
        komponent_educational_programs = KomponentEducationalPrograms.objects.get(id=pk)
    except KomponentEducationalPrograms.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
            )
        return redirect('update_educational_programs', pk=komponent_educational_programs.educationalProgram.id)

    komponent_educational_programs.delete()
    messages.success(
            request, 'Komponent educational programs deleted successfully'
            )
    return redirect('update_educational_programs', pk=komponent_educational_programs.educationalProgram.id)

class EducationalProgramsDelete(DeleteView):
    model = EducationalPrograms
    success_url='/control/educational-programs-create-or-update/'
    template_name = "educational_programs/educational_programs_delete.html"