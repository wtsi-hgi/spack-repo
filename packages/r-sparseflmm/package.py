# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparseflmm(RPackage):
	"""Functional Linear Mixed Models for Irregularly or Sparsely
Sampled Data

	Estimation of functional linear mixed models for irregularly or
    sparsely sampled data based on functional principal component analysis.
	"""
	
	cran = "sparseFLMM" 

	version("0.4.1", md5="2bb5766710c1e7ac44ab8f5d6be98175")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mgcv@1.8.12:", type=("build", "run"))
	depends_on("r-refund@0.1.22:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
