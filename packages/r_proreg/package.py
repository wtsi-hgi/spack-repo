# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProreg(RPackage):
	"""Patient Reported Outcomes Regression Analysis

	It offers a wide variety of techniques, such as graphics, recoding, or regression models, for a comprehensive analysis of patient-reported outcomes (PRO). Especially novel is the broad range of regression models based on the beta-binomial distribution useful for analyzing binomial data with over-dispersion in cross-sectional, longitudinal, or multidimensional response studies (see Najera-Zuloaga J., Lee D.-J. and Arostegui I. (2019) <doi:10.1002/bimj.201700251>).
	"""
	
	cran = "PROreg" 

	version("1.3", md5="e154b32a072180edfc23649e31600a52")
	version("1.2", md5="4b909bbfc279b6a8b844b07007c94e33")

	depends_on("r-fmsb", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
