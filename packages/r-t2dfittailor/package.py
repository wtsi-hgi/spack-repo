# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RT2dfittailor(RPackage):
	"""'Tailor the Exercise Plans and Visualize the Outcome for T2D
Patients'

	A system for personalized exercise plan recommendations for T2D (Type 2 Diabetes) patients  based on the primary outcome of HbA1c (Glycated Hemoglobin). You provide the individual's information, and 'T2DFitTailor' details the exercise plan and predicts the intervention's effectiveness.
	"""
	
	cran = "T2DFitTailor" 

	version("1.0.0", md5="28adc1fd7ce6176cd8bfb3607eaa4444")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
