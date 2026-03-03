# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDive(RPackage):
	"""Diversity Estimator

	Contains functions for the 'DivE' estimator <doi:10.1371/journal.pcbi.1003646>. The 'DivE' estimator is a heuristic approach to estimate the number of classes or the number of species (species richness) in a population. 
	"""
	
	cran = "DivE" 

	version("1.3", md5="988be0fb429fa49f2a7d9e7711d0c7d3")

	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-fme", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r@2.15.3:", type=("build", "run"))
