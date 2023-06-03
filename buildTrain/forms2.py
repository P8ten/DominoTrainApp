from django import forms
from django.utils.safestring import mark_safe
from django.templatetags.static import static


class ImageRadioSelect(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):

        context = self.get_context(name, value, attrs)
        print(context)
        # Initialize the output string
        output = []

        # Iterate over the choices
        for i, (option_value, option_label) in enumerate(self.choices):
            # Add a radio button for the choice
            radio = f'<input name="{name}" value="{option_value}" id="{name}_{i}">'

            # Add the image for the choice
            img_url = static(f'buildTrain/images/{option_label}')
            img = f'<label for="{name}_{i}"><img src="{img_url}"></label>'

            # Combine the radio button and image and add it to the output
            output.append(mark_safe(f'<div class="radio">{radio}{img}</div>'))

        # Combine all the output and return
        #return mark_safe('\n'.join(output))
    
        return self._render(self.template_name, context, renderer)



class StationForm(forms.Form):
    nums = 8
    choices = [(n, f'{n}_{n}.png') for n in range(nums + 1)]
    station = forms.ChoiceField(widget=ImageRadioSelect(attrs={'class':"form-check-input"}), choices=choices)


