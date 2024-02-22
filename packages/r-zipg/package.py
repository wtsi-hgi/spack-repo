# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZipg(RPackage):
	"""Zero-Inflated Poisson-Gamma Regression

	We provide a flexible Zero-inflated Poisson-Gamma Model (ZIPG) by connecting both the mean abundance and the variability to different covariates, and build valid statistical inference procedures for both parameter estimation and hypothesis testing. These functions can be used to analyze microbiome count data with zero-inflation and overdispersion. The model is discussed in Jiang et al (2023) <doi:10.1080/01621459.2022.2151447>.
	"""
	
	homepage = "https://github.com/roulan2000/ZIPG"
	cran = "ZIPG" 

	version("1.1", md5="ec6c2d72c61369ddb874e3c5c95fd541")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
