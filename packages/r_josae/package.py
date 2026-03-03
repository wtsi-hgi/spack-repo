# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJosae(RPackage):
	"""Unit-Level and Area-Level Small Area Estimation

	Implementation of some unit and area level EBLUP estimators as well as the estimators of their MSE also under heteroscedasticity. The package further documents the publications Breidenbach and Astrup (2012) <DOI:10.1007/s10342-012-0596-7>, Breidenbach et al. (2016) <DOI:10.1016/j.rse.2015.07.026> and Breidenbach et al. (2018 in press). The vignette further explains the use of the implemented functions.
	"""
	
	cran = "JoSAE" 

	version("0.3.0", md5="247f0c1d0a5acf34fab9d66b8fc6e78e")

	depends_on("r-nlme", type=("build", "run"))
