# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpgfilter(RPackage):
	"""CpG Filtering Method Based on Intra-Class Correlation
Coefficients

	Filter CpGs based on Intra-class Correlation Coefficients (ICCs) when replicates are available. ICCs are calculated by fitting linear mixed effects models to all samples including the un-replicated samples. Including the large number of un-replicated samples improves ICC estimates dramatically. The method accommodates any replicate design. 
	"""
	
	cran = "CpGFilter" 

	version("1.1", md5="f9f2d5b2de857df100f05dd30af1d4d1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
