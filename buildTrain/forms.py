from django import forms
from django.utils.safestring import mark_safe
from django.templatetags.static import static


class ImageRadioSelect(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):

        context = super(ImageRadioSelect, self).get_context(name, value, attrs)
        # Initialize the output string
        output = []
        print(context)
        print('---------------------------')
        print(attrs)

        class_input = context['widget']['attrs']['class_input']

        # Iterate over the choices
        for i, (option_value, option_label) in enumerate(self.choices):
            # Add a radio button for the choice
            input = f'<input name="{name}" type="radio" value="{option_value}" id="{name}_{i}" />'

            # Add the image for the choice
            # img_url = static(f'buildTrain/images/{option_label}')
            # img = f'<img class="test" src="{img_url}">'

            label = f'<label class="domino d{option_label}" for="{name}_{i}"></label>'

            # Combine the radio button and image and add it to the output
            output.append(mark_safe(f'{input}{label}'))

        # Combine all the output and return
        return mark_safe('\n'.join(output))
        # print(context)
        # return self._render(self.template_name, context, renderer)



class StationForm(forms.Form):
    nums = 8
    choices = [(n, f'{n}_{n}') for n in range(nums + 1)]
    station = forms.ChoiceField(
        widget=ImageRadioSelect(
            attrs={
                'class_input': 'form-check-input',
                }
        ), 
        choices=choices
    )


