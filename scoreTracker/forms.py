from django import forms



from .models import *
class PostForm(forms.ModelForm):
    # class Meta:
    def __init__(self, *args, **kwargs):
        super(PostForm,self).__init__(*args, **kwargs)
        choice=tuple([(i.PlayerName,i.PlayerName)for i in Ludo.objects.all()])
        self.fields['First'] =forms.ChoiceField(choices=choice)
        self.fields['Second'] =forms.ChoiceField(choices=choice)
        self.fields['Third'] =forms.ChoiceField(choices=choice)
        self.fields['Fourth'] =forms.ChoiceField(choices=choice)

    class Meta:
        # fdescription = forms.CharField(max_length=2000,
        # widget=forms.Textarea() )
        model = History
        fields = ('First','Second','Third','Fourth',)
        

class PlayerForm(forms.ModelForm):
    class Meta:
        model=Ludo
        fields= ('PlayerName','MatchesPlayed','TotalScore','Average')
        # widgets = {'MatchesPlayed': forms.HiddenInput(),'TotalScore': forms.HiddenInput(),'Average': forms.HiddenInput()}

# class AddUser(forms.ModelForm):
#     model=Ludo