from django import forms





class ContactForm(forms.Form):
    fullname = forms.CharField(max_length= 100 , label = 'Full Name', 
                               widget = forms.TextInput(attrs={'class':'form - control',      
                               'placeholder':'Enter your full name'}))
    email = forms .EmailField(label='Email',
                              widget=forms.EmailInput(attrs={'class': 'form-control',
                                'placeholder':'Enter your email'}))
    massage= forms.CharField(label='Massage',
                             widget=forms.Textarea(attrs={'class':'form-control',
                              'placeholder':'Enter your massage' }))
                     

    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if len (fullname) < 5:
            raise forms.ValidationError('Full name must be more than 5 characters')
        
        return fullname
    

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError('Message must be more than 10 characters')
        


# class BlogForm(forms.ModelForm):
#     class Meta:
#         model = Blogs
#         fields = '__all__'
#         widgets ={
#             'title': forms.TextInput(attrs= {'class': 'form-control' , 'placefolder': 'Enter the title of the blog' })
#         }