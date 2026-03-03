# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFcopulae(RPackage):
	"""Rmetrics - Bivariate Dependence Structures with Copulae

	Provides a  collection of functions to 
	manage, to investigate and to analyze bivariate financial returns by  
	Copulae. Included are the families of Archemedean, Elliptical, 
	Extreme Value, and Empirical Copulae.
	"""
	
	homepage = "https://www.rmetrics.org"
	cran = "fCopulae" 

	version("4022.85", md5="d2e0e2fbb26e47a25ede6b7810c966bd")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-fmultivar", type=("build", "run"))
