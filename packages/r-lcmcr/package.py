# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcmcr(RPackage):
	"""Bayesian Non-Parametric Latent-Class Capture-Recapture

	Bayesian population size estimation using non parametric latent-class models.
	"""
	
	cran = "LCMCR" 

	version("0.4.14", md5="2c93527de37e196ff7ad60de5067d2bf")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("gsl@2.5:", type=("build", "link", "run"))
