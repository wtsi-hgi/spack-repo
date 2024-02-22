# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvmi(RPackage):
	"""Multiple Imputation Method in Survival Analysis

	In clinical trials, endpoints are sometimes evaluated with uncertainty. Adjudication is commonly adopted to ensure the study integrity. We propose to use multiple imputation (MI) introduced by Robin (1987) <doi:10.1002/9780470316696> to incorporate these uncertainties if reasonable event probabilities were provided. The method has been applied to Cox Proportional Hazard (PH) model, Kaplan-Meier (KM) estimation and Log-rank test in this package. Moreover, weighted estimations discussed in Cook (2004) <doi:10.1016/S0197-2456(00)00053-2> were also implemented with weights calculated from event probabilities. In conclusion, this package can handle time-to-event analysis if events presented with uncertainty by different methods. 
	"""
	
	cran = "SurvMI" 

	version("0.1.0", md5="1b1a09cc921094cd6baffd17a58af865")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival@3.1.11:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
