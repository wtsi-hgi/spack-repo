# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoistweedie(RPackage):
	"""Poisson-Tweedie Exponential Family Models

	Simulation of models Poisson-Tweedie.
	"""
	
	homepage = "https://CRAN.R-project.org/package=poistweedie"
	cran = "poistweedie" 

	version("1.0.2", md5="6082be83ad62e75a7eaaa765e2311a6d")

	depends_on("r@2.10:", type=("build", "run"))
