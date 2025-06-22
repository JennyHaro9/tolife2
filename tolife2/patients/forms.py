from django import forms


class ClinicalParameterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Fecha de inicio",
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"}),
        label="Fecha de fin",
    )
    category = forms.ChoiceField(
        choices=[
            ("environment", "Environment"),
            ("mic", "Mic"),
            ("sleep_quality", "Sleep Quality"),
            ("rf", "RF"),
            ("hr", "HR"),
            ("mobility", "Mobility"),
            ("ppg_watch", "PPG Watch"),
            ("spirometer", "Spirometer"),
            ("cat", "CAT"),
            ("ccq", "CCQ"),
            ("mmrc", "mMRC"),
        ],
        initial="environment",
        label="Categoría",
    )
