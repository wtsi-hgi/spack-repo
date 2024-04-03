# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcpb(RPackage):
	"""Longitudinal PB Varying-Coefficient Groupwise Disparity Model

	Estimating the disparity between two groups based on the extended model of the Peters-Belson (PB) method. Our model is the first work on the longitudinal data, and also can set a varying variable to find the complicated association between other variables and the varying variable. Our work is an extension of the Peters-Belson method which was originally published in Peters (1941)<doi:10.1080/00220671.1941.10881036> and Belson (1956)<doi:10.2307/2985420>.
	"""
	
	homepage = "https://github.com/SangkyuStat/vcPB"
	cran = "vcPB" 

	version("1.1.1", md5="7382aab1eb5b58f071ae40ca8eb0adec")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
