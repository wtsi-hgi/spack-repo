# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoynam(RPackage):
	"""Soybean Nested Association Mapping Dataset

	Genomic and multi-environmental soybean data. Soybean Nested
    Association Mapping (SoyNAM) project dataset funded by the United Soybean Board
    (USB). BLUP function formats data for genome-wide prediction and association analysis.
	"""
	
	cran = "SoyNAM" 

	version("1.6.2", md5="2077ba8872b98452f848d343fa417d3f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nam", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
