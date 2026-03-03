# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocus(RPackage):
	"""Low-Rank Decomposition of Brain Connectivity Matrices with
Uniform Sparsity

	To decompose symmetric matrices such as brain connectivity matrices so that one can extract sparse latent component matrices and also estimate mixing coefficients, a blind source separation (BSS) method named LOCUS was proposed in Wang and Guo (2023) <arXiv:2008.08915>. For brain connectivity matrices, the outputs correspond to sparse latent connectivity traits and individual-level trait loadings. 
	"""
	
	cran = "LOCUS" 

	version("1.0", md5="801397b8f274e27922d21a46611080fd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-far", type=("build", "run"))
