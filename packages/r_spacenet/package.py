# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpacenet(RPackage):
	"""Latent Space Models for Multidimensional Networks

	Latent space models for multivariate networks (multiplex) estimated via MCMC algorithm. See D Angelo et al. (2018) <arXiv:1803.07166> and D Angelo et al. (2018) <arXiv:1807.03874>.
	"""
	
	cran = "spaceNet" 

	version("1.2", md5="efb62088be8e21ef5ff9cca37b1be10c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust@5.3:", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-rcpptn", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-sna", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
