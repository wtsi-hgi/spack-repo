# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnlttsa(RPackage):
	"""Complex-Valued Wavelet Lifting for Univariate and Bivariate Time
Series Analysis

	Implementations of recent complex-valued wavelet spectral procedures for analysis of irregularly sampled signals, see Hamilton et al (2018) <doi:10.1080/00401706.2017.1281846>.
	"""
	
	cran = "CNLTtsa" 

	version("0.1-2", md5="8424708f6dd958bb42eed90794864e10")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-adlift", type=("build", "run"))
	depends_on("r-nlt", type=("build", "run"))
	depends_on("r-cnltreg", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
