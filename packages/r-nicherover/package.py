# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNicherover(RPackage):
	"""Niche Region and Niche Overlap Metrics for Multidimensional
Ecological Niches

	Implementation of a probabilistic method to calculate 'nicheROVER' (_niche_ _r_egion and niche _over_lap) metrics using multidimensional niche indicator data (e.g., stable isotopes, environmental variables, etc.). The niche region is defined as the joint probability density function of the multidimensional niche indicators at a user-defined probability alpha (e.g., 95%).  Uncertainty is accounted for in a Bayesian framework, and the method can be extended to three or more indicator dimensions.  It provides directional estimates of niche overlap, accounts for species-specific distributions in multivariate niche space, and produces unique and consistent bivariate projections of the multivariate niche region.  The article by Swanson et al. (2015) <doi:10.1890/14-0235.1> provides a detailed description of the methodology.  See the package vignette for a worked example using fish stable isotope data.
	"""
	
	homepage = "https://github.com/mlysy/nicheROVER"
	cran = "nicheROVER" 

	version("1.1.2", md5="55703e091d11c974788a7427c065a899")

	depends_on("r@1.9:", type=("build", "run"))
