# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirmcmc(RPackage):
	"""Directional Metropolis Hastings Algorithm

	Implementation of Directional Metropolis Hastings Algorithm for
    MCMC.
	"""
	
	cran = "dirmcmc" 

	version("1.3.3", md5="3c999febb1b75623e0989933b668a049")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mcmcse", type=("build", "run"))
