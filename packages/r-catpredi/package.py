# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatpredi(RPackage):
	"""Optimal Categorisation of Continuous Variables in Prediction
Models

	Allows the user to categorise a continuous predictor variable in a logistic or a Cox proportional hazards regression setting, by maximising the discriminative ability of the model. I Barrio, I Arostegui, MX Rodriguez-Alvarez, JM Quintana (2015) <doi:10.1177/0962280215601873>. I Barrio,  MX Rodriguez-Alvarez, L Meira-Machado, C Esteban, I Arostegui (2017) <https://www.idescat.cat/sort/sort411/41.1.3.barrio-etal.pdf>.
	"""
	
	cran = "CatPredi" 

	version("1.3", md5="aee09bc45be458b2f0205b90829720f2")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
