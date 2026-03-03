# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonpca(RPackage):
	"""Poisson-Noise Corrected PCA

	For a multivariate dataset with independent Poisson measurement error, calculates principal components of transformed latent Poisson means. T. Kenney, T. Huang, H. Gu (2019) <arXiv:1904.11745>.
	"""
	
	cran = "PoissonPCA" 

	version("1.0.3", md5="0c2f22b60a8e1ca6b8a77dacb90653ca")

	depends_on("r@3.2.3:", type=("build", "run"))
