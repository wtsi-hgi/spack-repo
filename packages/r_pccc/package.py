# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPccc(RPackage):
	"""Pediatric Complex Chronic Conditions

	An implementation of the pediatric complex chronic conditions (CCC)
    classification system using R and C++.
	"""
	
	homepage = "https://github.com/CUD2V/pccc"
	cran = "pccc" 

	version("1.0.5", md5="e8b3e075deb5028683b955c83d3f2e84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rcpp@0.12.11:", type=("build", "run"))
