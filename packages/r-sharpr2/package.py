# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharpr2(RPackage):
	"""Estimating Regulatory Scores and Identifying ATAC-STARR Data

	An algorithm for identifying high-resolution driver elements for datasets from a high-definition reporter assay library. Xinchen Wang, Liang He, Sarah Goggin, Alham Saadat, Li Wang, Melina Claussnitzer, Manolis Kellis (2017) <doi:10.1101/193136>.
	"""
	
	cran = "sharpr2" 

	version("1.1.1.0", md5="f784ae207bea91de7a24d25b581454c1", url="https://cran.r-project.org/src/contrib/sharpr2_1.1.1.0.tar.gz")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mvtnorm@1:", type=("build", "run"))
	depends_on("r-matrix@1.2:", type=("build", "run"))
