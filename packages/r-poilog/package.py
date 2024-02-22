# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoilog(RPackage):
	"""Poisson Lognormal and Bivariate Poisson Lognormal Distribution

	Functions for obtaining the density, random deviates 
             and maximum likelihood estimates of the Poisson lognormal 
             distribution and the bivariate Poisson lognormal distribution.
	"""
	
	cran = "poilog" 

	version("0.4.2", md5="e3eaf4f8caf52dc896096364e3de4dee")

