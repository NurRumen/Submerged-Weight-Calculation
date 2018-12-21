from django.shortcuts import render
from .forms import InputForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            pipe_outside_diameter = form.cleaned_data['pipe_outside_diameter']
            pipe_wall_thickness = form.cleaned_data['pipe_wall_thickness']
            pipe_density = form.cleaned_data['pipe_density']
            corrosion_density = form.cleaned_data['corrosion_density']
            external_coating_thickness = form.cleaned_data['external_coating_thickness']
            external_coating_density = form.cleaned_data['external_coating_density']
            installation_empty_air = form.cleaned_data['installation_empty_air']
            flooded_water = form.cleaned_data['flooded_water']
            hydrotest_sea_water = form.cleaned_data['hydrotest_sea_water']

            inside_diameter = float(pipe_outside_diameter)-(2*float(pipe_wall_thickness))
            inside_radious = inside_diameter/2
            outer_radious = float(pipe_outside_diameter)/2
            coating_density = (float(pipe_outside_diameter)+float(external_coating_thickness))/2
            # pipeline_diameter = (float(pipe_outside_diameter)+float(external_coating_thickness))
            pipeline_diameter = coating_density*2
            pipe_weight_per_unit = ((3.14159/4)*float(pipe_density)*((float(pipe_outside_diameter)*float(pipe_outside_diameter))-(float(inside_diameter)*float(inside_diameter))))/144
            coating_weight_per_unit = ((3.14159/4)*float(external_coating_density)*((float(pipeline_diameter)*float(pipeline_diameter))-(float(pipe_outside_diameter)*float(pipe_outside_diameter))))/144
            contents_weight_per_unit = ((3.14159/4)*float(installation_empty_air)*(float(inside_diameter)*float(inside_diameter)))/144
            total_weight_per_unit = pipe_weight_per_unit + coating_weight_per_unit + contents_weight_per_unit
            buoyant_per_unit = ((3.14159/4)*float(pipeline_diameter)*(float(pipeline_diameter)*float(hydrotest_sea_water)))/144
            submerged_weight = total_weight_per_unit - buoyant_per_unit
            specific_gravity = total_weight_per_unit/buoyant_per_unit

            return render(request, 'db.html', {'inside_radious': inside_radious,
                                               'outer_radious': outer_radious,
                                               'coating_density': coating_density,
                                               'pipeline_diameter': pipeline_diameter,
                                               'pipe_weight_per_unit': pipe_weight_per_unit,
                                               'coating_weight_per_unit': coating_weight_per_unit,
                                               'contents_weight_per_unit': contents_weight_per_unit,
                                               'total_weight_per_unit': total_weight_per_unit,
                                               'buoyant_per_unit': buoyant_per_unit,
                                               'submerged_weight': submerged_weight,
                                               'specific_gravity': specific_gravity,
                                               })

        else:
            return HttpResponse('Submission Error! Please Submit Again.')


    else:
        form = InputForm()
    return render(request, 'index.html', {'form': form})
