# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLda(RPackage):
	"""Collapsed Gibbs Sampling Methods for Topic Models

	Implements latent Dirichlet allocation (LDA)
	     and related models.  This includes (but is not limited
	     to) sLDA, corrLDA, and the mixed-membership stochastic
	     blockmodel.  Inference for all of these models is
	     implemented via a fast collapsed Gibbs sampler written
	     in C.  Utility functions for reading/writing data
	     typically used in topic models, as well as tools for
	     examining posterior distributions are also included.
	"""
	
	cran = "lda" 

	version("1.4.2", md5="c48a92925fd43592efd14cac12ff1c5d")

	depends_on("r@2.10:", type=("build", "run"))
