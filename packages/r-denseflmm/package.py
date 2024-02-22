# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenseflmm(RPackage):
	"""Functional Linear Mixed Models for Densely Sampled Data

	Estimation of functional linear mixed models for densely sampled data based on functional principal component analysis.
	"""
	
	cran = "denseFLMM" 

	version("0.1.2", md5="f4ac1dd065276ac3b369b3ec11bef628")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mgcv@1.8.12:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
