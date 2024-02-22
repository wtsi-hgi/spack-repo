# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCobiclust(RPackage):
	"""Biclustering via Latent Block Model Adapted to Overdispersed
Count Data

	Implementation of a probabilistic method for biclustering
    adapted to overdispersed count data. It is a Gamma-Poisson Latent
    Block Model.  It also implements two selection criteria in order to
    select the number of biclusters.
	"""
	
	homepage = "https://github.com/julieaubert/cobiclust"
	cran = "cobiclust" 

	version("0.1.2", md5="403fc4801b73d4357eea2d32ded0790f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
