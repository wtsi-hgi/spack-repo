# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmest(RPackage):
	"""Generalized Latent Markov Models

	Latent Markov models for longitudinal continuous and categorical data. See Bartolucci, Pandolfi, Pennoni (2017)<doi:10.18637/jss.v081.i04>.
	"""
	
	cran = "LMest" 

	version("3.1.2", md5="78bce4659c3eaa1d50ce7986da84b2d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-multilcirt", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-formula@1.2.3:", type=("build", "run"))
	depends_on("r-mix", type=("build", "run"))
	depends_on("r-diagram@1.6.4:", type=("build", "run"))
	depends_on("r-mclust@5.4.6:", type=("build", "run"))
	depends_on("r-scatterplot3d@0.3.41:", type=("build", "run"))
