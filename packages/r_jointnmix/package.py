# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointnmix(RPackage):
	"""Joint N-Mixture Models for Site-Associated Species

	Fits univariate and joint N-mixture models for data on two unmarked site-associated species. Includes functions to estimate latent abundances through empirical Bayes methods.
	"""
	
	cran = "jointNmix" 

	version("1.0", md5="6e70e4644c7401bf083fe5fa231d3777")

	depends_on("r@3:", type=("build", "run"))
