# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcmod(RPackage):
	"""Informative Procrustean Matrix Correlation

	Estimates corrected Procrustean correlation between matrices for removing overfitting effect. Coissac Eric and Gonindard-Melodelima Christelle (2019) <doi:10.1101/842070>.
	"""
	
	cran = "ProcMod" 

	version("1.0.8", md5="4bd1332c70b7a178d52515f3f2db87f9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
