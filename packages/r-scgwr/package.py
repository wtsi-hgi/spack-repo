# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScgwr(RPackage):
	"""Scalable Geographically Weighted Regression

	Fast and regularized version of GWR for large dataset, detailed in Murakami, Tsutsumida, Yoshida, Nakaya, and Lu (2019) <arXiv:1905.00266>.
	"""
	
	cran = "scgwr" 

	version("0.1.2-21", md5="93bf67bb9f11d4e806ff7d434d477972")

	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-spdata", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-optimparallel", type=("build", "run"))
