# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTropfishr(RPackage):
	"""Tropical Fisheries Analysis

	A compilation of fish stock assessment methods for the
    analysis of length-frequency data in the context of data-poor
    fisheries. Includes methods and examples included in the FAO
    Manual by P. Sparre and S.C. Venema (1998), "Introduction to tropical fish
    stock assessment" (<https://www.fao.org/documents/card/en/c/9bb12a06-2f05-5dcb-a6ca-2d6dd3080f65/>),
    as well as other more recent methods.
	"""
	
	homepage = "https://github.com/tokami/TropFishR"
	cran = "TropFishR" 

	version("1.6.4", md5="dacbb8389bb2b7c5aec44c4eeccdef00")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-propagate", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
