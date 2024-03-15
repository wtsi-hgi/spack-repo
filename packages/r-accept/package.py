# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccept(RPackage):
	"""The Acute COPD Exacerbation Prediction Tool (ACCEPT)

	Allows clinicians to predict the rate and severity of future acute exacerbation in Chronic Obstructive Pulmonary Disease (COPD) patients, based on the clinical prediction models published in Adibi et al. (2020) <doi:10.1016/S2213-2600(19)30397-2> and Safari et al. (2022) <doi:10.1016/j.eclinm.2022.101574>. 
	"""
	
	cran = "accept" 

	version("1.0.0", md5="4885f0c4036a0a76cfab59b42d81e3e6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reldist", type=("build", "run"))
