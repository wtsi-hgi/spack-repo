# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmml(RPackage):
	"""Generalized Linear Models with Clustering

	Binomial and Poisson regression for clustered data, fixed
        and random effects with bootstrapping.
	"""
	
	cran = "glmmML" 

	version("1.1.6", md5="e39afdfe3dcd00e6e1bbd6d91059cc82")

	depends_on("r@2.13:", type=("build", "run"))
