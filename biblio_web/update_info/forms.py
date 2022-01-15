from django import forms

class UpdateDocInfoForm(forms.Form):
    # entity = "name", "entity_type" ['organization'], "connection_type" ['Company','Author', 'Creator', 'Author', "Contributor", "Publisher"]
    # tags = forms.CharField(
    #     required=False,
    #     label="tags",
    #     help_text="A comma separated list of tags to assign to the document.",
    # )
    title = forms.CharField(
        required=True,
        label="title",
        help_text="The title of the document.",
    )
    language = forms.CharField(
        required=False,
        label="language",
        help_text="The language of the document.",
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows":6}),
        required=False,
        label="description",
        help_text="A description of the document.",
    )
    source = forms.CharField(
        required=False,
        label="source",
        help_text="The source where you got the document.",
    )
    date = forms.CharField(
        required=False,
        label="date",
        help_text="The date the document was created on.",
    )
    license = forms.CharField(
        required=False,
        label="license",
        help_text="The license the document is under.",
    )
    rights = forms.CharField(
        required=False,
        label="rights",
        help_text="The rights statement/license statement to use for the document.",
    )
