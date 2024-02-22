# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastfmm(RPackage):
	"""Fast Functional Mixed Models using Fast Univariate Inference

	Implementation of the fast univariate inference approach (Cui et al. (2022) <doi:10.1080/10618600.2021.1950006>, Loewinger et al. (2023) <doi:10.1101/2023.11.06.565896>) for fitting functional mixed models.
	"""
	
	homepage = "https://github.com/gloewing/fastFMM"
	cran = "fastFMM" 

	version("0.2.0", md5="f6c025b1b2522763476915fc0eeccfc4")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-caic4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lsei", type=("build", "run"))
	depends_on("r-refund", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-lmeresampler", type=("build", "run"))
