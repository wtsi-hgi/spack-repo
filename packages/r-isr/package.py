# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsr(RPackage):
	"""The Iterated Score Regression-Based Estimation Algorithm

	Algorithm to handle with PCA-based missing data, where ISR is for PCA-based missing data with high correlation and DISR is for distributed PCA-based missing data. The philosophy of the package is described in Guo G. (2020) <doi:10.1080/02331888.2020.1823979>. 
	"""
	
	cran = "ISR" 

	version("2022.4.22", md5="95e916442fd265c82ff342ff58739533")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
