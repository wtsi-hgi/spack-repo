# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoxicpen(RPackage):
	"""Variable Selection for Cox's Model with Interval-Censored Data

	Perform variable selection for Cox regression model with interval-censored data. Can deal with both low-dimensional and high-dimensional data. Case-cohort design can be incorporated. Two sets of covariates scenario can also be considered. The references are listed in the URL below.
	"""
	
	homepage = "https://doi.org/10.1080/01621459.2018.1537922"
	cran = "CoxICPen" 

	version("1.1.0", md5="e0b2019a83987539b7581a838193b9da")

	depends_on("r-foreach", type=("build", "run"))
