from django import forms
from online_shop.models import Comment, Order,Product


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('product',)

    def clean_email(self):
        email = self.data.get('email')
        if Comment.objects.filter(email=email).exists():
            raise forms.ValidationError(f'This {email} is already used')
        return email


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('product',)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'