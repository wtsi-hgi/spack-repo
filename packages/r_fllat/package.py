# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFllat(RPackage):
	"""Fused Lasso Latent Feature Model

	Fits the Fused Lasso Latent Feature model, which is used for modeling multi-sample aCGH data to identify regions of copy number variation (CNV).  Produces a set of features that describe the patterns of CNV and a set of weights that describe the composition of each sample.  Also provides functions for choosing the optimal tuning parameters and the appropriate number of features, and for estimating the false discovery rate.
	"""
	
	cran = "FLLat" 

	version("1.2-1", md5="79f3eec5f7e72213c5be8c0710342e80")

	depends_on("r-gplots", type=("build", "run"))
