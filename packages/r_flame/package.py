# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlame(RPackage):
	"""Interpretable Matching for Causal Inference

	Efficient implementations of the algorithms in the 
    Almost-Matching-Exactly framework for interpretable matching in causal
    inference. These algorithms match units via a learned, weighted Hamming
    distance that determines which covariates are more important to match on.
    For more information and examples, see the Almost-Matching-Exactly website. 
	"""
	
	homepage = "https://almost-matching-exactly.github.io"
	cran = "FLAME" 

	version("2.1.1", md5="b786c33e5e14ab944acdc120d135c95a")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
