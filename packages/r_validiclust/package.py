# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValidiclust(RPackage):
	"""VALID Inference for Clusters Separation Testing

	Given a partition resulting from any clustering algorithm, the implemented tests allow valid post-clustering inference by testing if a given variable significantly separates two of the estimated clusters. 
             Methods are detailed in: Hivert B, Agniel D, Thiebaut R & Hejblum BP (2022). 
             "Post-clustering difference testing: valid inference and practical considerations", <arXiv:2210.13172>.
	"""
	
	cran = "VALIDICLUST" 

	version("0.1.0", md5="c2f40611cec7fa2bc5dbd762b6aa07c8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
