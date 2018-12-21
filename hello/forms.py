from django import forms


class InputForm(forms.Form):
    pipe_outside_diameter = forms.CharField(max_length=10, required=False, initial='10.75')
    pipe_wall_thickness = forms.CharField(max_length=10, required=False, initial='0.5')
    pipe_density = forms.CharField(max_length=10, required=False, initial='490')
    corrosion_density = forms.CharField(max_length=10, required=False, initial='0.125')
    external_coating_thickness = forms.CharField(max_length=10, required=False, initial='0.0118')
    external_coating_density = forms.CharField(max_length=10, required=False, initial='81.16')
    installation_empty_air = forms.CharField(max_length=10, required=False, initial='0')
    flooded_water = forms.CharField(max_length=10, required=False, initial='64')
    hydrotest_sea_water = forms.CharField(max_length=10, required=False, initial='64.7')


    def clean(self):
        cleaned_data = super(InputForm, self).clean()
        pipe_outside_diameter = cleaned_data.get('pipe_outside_diameter')
        pipe_wall_thickness = cleaned_data.get('pipe_wall_thickness')
        pipe_density = cleaned_data.get('pipe_density')
        corrosion_density = cleaned_data.get('corrosion_density')
        external_coating_thickness = cleaned_data.get('external_coating_thickness')
        external_coating_density = cleaned_data.get('external_coating_density')
        installation_empty_air = cleaned_data.get('installation_empty_air')
        flooded_water = cleaned_data.get('flooded_water')
        hydrotest_sea_water = cleaned_data.get('hydrotest_sea_water')

    # def clean(self):
    #     if not self['name'].html_name in self.data:
    #         return self.fields['name'].initial
    #     return self.cleaned_data['name']
