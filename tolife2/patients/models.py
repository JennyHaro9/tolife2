from django.db import models

from tolife2.users.models import Doctor


class Patient(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=50, unique=True)
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name="patients",
        null=True,
    )

    def __str__(self):
        return f"{self.name} ({self.identifier})"


class ClinicalParameter(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()

    # --- Environment - Día ---
    mean_temp_day = models.FloatField(null=True, blank=True)
    std_temp_day = models.FloatField(null=True, blank=True)
    min_temp_day = models.FloatField(null=True, blank=True)
    max_temp_day = models.FloatField(null=True, blank=True)

    mean_lux_day = models.FloatField(null=True, blank=True)
    std_lux_day = models.FloatField(null=True, blank=True)
    min_lux_day = models.FloatField(null=True, blank=True)
    max_lux_day = models.FloatField(null=True, blank=True)

    mean_hum_day = models.FloatField(null=True, blank=True)
    std_hum_day = models.FloatField(null=True, blank=True)
    min_hum_day = models.FloatField(null=True, blank=True)
    max_hum_day = models.FloatField(null=True, blank=True)

    mean_aqi_day = models.FloatField(null=True, blank=True)
    std_aqi_day = models.FloatField(null=True, blank=True)
    min_aqi_day = models.FloatField(null=True, blank=True)
    max_aqi_day = models.FloatField(null=True, blank=True)

    # --- Environment - Noche ---
    mean_temp_night = models.FloatField(null=True, blank=True)
    std_temp_night = models.FloatField(null=True, blank=True)
    min_temp_night = models.FloatField(null=True, blank=True)
    max_temp_night = models.FloatField(null=True, blank=True)

    mean_lux_night = models.FloatField(null=True, blank=True)
    std_lux_night = models.FloatField(null=True, blank=True)
    min_lux_night = models.FloatField(null=True, blank=True)
    max_lux_night = models.FloatField(null=True, blank=True)

    mean_hum_night = models.FloatField(null=True, blank=True)
    std_hum_night = models.FloatField(null=True, blank=True)
    min_hum_night = models.FloatField(null=True, blank=True)
    max_hum_night = models.FloatField(null=True, blank=True)

    mean_aqi_night = models.FloatField(null=True, blank=True)
    std_aqi_night = models.FloatField(null=True, blank=True)
    min_aqi_night = models.FloatField(null=True, blank=True)
    max_aqi_night = models.FloatField(null=True, blank=True)

    index_validity_env = models.BooleanField(default=True)
    data_validity_env = models.BooleanField(default=True)

    # --- Categoría: Mic ---
    mean_si = models.FloatField(null=True, blank=True)
    std_si = models.FloatField(null=True, blank=True)
    min_si = models.FloatField(null=True, blank=True)
    max_si = models.FloatField(null=True, blank=True)

    index_validity_mic = models.BooleanField(default=True)
    data_validity_mic = models.BooleanField(default=True)

    # --- Categoría: Sleep Quality ---
    sleep_efficiency = models.FloatField(null=True, blank=True)
    num_movements = models.IntegerField(null=True, blank=True)
    hours_bed = models.FloatField(null=True, blank=True)
    total_movement = models.FloatField(null=True, blank=True)
    index_validity_sleep = models.BooleanField(default=True)
    data_validity_sleep = models.BooleanField(default=True)
    # --- Categoría: RF ---
    rf_mean = models.FloatField(null=True, blank=True)
    rf_std = models.FloatField(null=True, blank=True)
    rf_min = models.FloatField(null=True, blank=True)
    rf_max = models.FloatField(null=True, blank=True)
    index_validity_rf = models.BooleanField(default=True)
    data_validity_rf = models.BooleanField(default=True)

    # --- Categoría: HR ---
    hr_mean = models.FloatField(null=True, blank=True)
    hr_std = models.FloatField(null=True, blank=True)
    hr_min = models.FloatField(null=True, blank=True)
    hr_max = models.FloatField(null=True, blank=True)
    index_validity_hr = models.BooleanField(default=True)
    data_validity_hr = models.BooleanField(default=True)

    # --- Categoría: Movility ---
    gs_mean = models.FloatField(null=True, blank=True)
    gs_std = models.FloatField(null=True, blank=True)
    smwd_mean = models.FloatField(null=True, blank=True)
    smwd_std = models.FloatField(null=True, blank=True)
    sl_mean = models.FloatField(null=True, blank=True)
    sl_std = models.FloatField(null=True, blank=True)
    walked_time = models.FloatField(null=True, blank=True)
    walked_distance = models.FloatField(null=True, blank=True)
    index_validity_movility = models.BooleanField(default=True)
    data_validity_movility = models.BooleanField(default=True)

    # --- Categoría: PPGWATCH  ---
    mean_hr = models.FloatField(null=True, blank=True)
    range_hr_low = models.FloatField(null=True, blank=True)
    range_hr_high = models.FloatField(null=True, blank=True)
    std_rr = models.FloatField(null=True, blank=True)
    range_stdrr_low = models.FloatField(null=True, blank=True)
    range_stdrr_high = models.FloatField(null=True, blank=True)
    rmssd = models.FloatField(null=True, blank=True)
    range_rmssd_low = models.FloatField(null=True, blank=True)
    range_rmssd_high = models.FloatField(null=True, blank=True)
    index_validity_ppg = models.BooleanField(default=True)
    data_validity_ppg = models.BooleanField(default=True)

    # --- Categoría: SpO2 ---
    mean_fev1 = models.FloatField(null=True, blank=True)
    range_fev1_low = models.FloatField(null=True, blank=True)
    range_fev1_high = models.FloatField(null=True, blank=True)
    mean_pef = models.FloatField(null=True, blank=True)
    range_pef_low = models.FloatField(null=True, blank=True)
    spo2 = models.FloatField(null=True, blank=True)
    hr = models.FloatField(null=True, blank=True)
    index_validity_spo2 = models.BooleanField(default=True)
    data_validity_spo2 = models.BooleanField(default=True)

    # --- Categoría: CAT ---
    cat = models.FloatField(null=True, blank=True)
    index_validity_cat = models.BooleanField(default=True)
    data_validity_cat = models.BooleanField(default=True)
    # --- Categoría: CCQ ---
    ccq = models.FloatField(null=True, blank=True)
    index_validity_ccq = models.BooleanField(default=True)
    data_validity_ccq = models.BooleanField(default=True)

    # --- Categoría: mmrc ---

    mmrc = models.FloatField(null=True, blank=True)
    index_validity_mmrc = models.BooleanField(default=True)
    data_validity_mmrc = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"
