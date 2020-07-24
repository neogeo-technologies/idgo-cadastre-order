# Copyright (c) 2017-2020 Neogeo-Technologies.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class Order(models.Model):

    class Meta(object):
        verbose_name = "Commande de fichiers fonciers"
        verbose_name_plural = "Commandes de fichiers fonciers"

    date = models.DateField(
        verbose_name="Date de la demande",
        null=True,
        auto_now_add=True,
        )

    STATUS_CHOICES = (
        (0, "En cours"),
        (1, "Validée"),
        (2, "Refusée"),
        )

    status = models.IntegerField(
        verbose_name="Statut de la demande",
        default=0,
        choices=STATUS_CHOICES,
        )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Demandeur",
        limit_choices_to={'profile__crige_membership': True}
        )

    ALLOWED_EXTENSIONS = ['pdf', 'png', 'doc', 'docx', 'odt']

    dpo_cnil = models.FileField(
        upload_to='idgo_cadastre_orders/',
        verbose_name="DPO CNIL*",
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])

    acte_engagement = models.FileField(
        upload_to='idgo_cadastre_orders/',
        verbose_name="Acte d'engagement*",
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS)])
