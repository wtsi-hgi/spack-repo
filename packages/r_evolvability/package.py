# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvolvability(RPackage):
	"""Calculation of Evolvability Parameters

	Provides tools for calculating evolvability parameters from estimated G-matrices as defined 
    in Hansen and Houle (2008) <doi:10.1111/j.1420-9101.2008.01573.x> and fits phylogenetic 
    comparative models that link the rate of evolution of a trait to the state of another evolving 
    trait (see Hansen et al. 2021 Systematic Biology <doi:10.1093/sysbio/syab079>). The package was 
    released with Bolstad et al. (2014) <doi:10.1098/rstb.2013.0255>, which contains some examples of use.
	"""
	
	cran = "evolvability" 

	version("2.0.0", md5="edca2385c59a06cfcc7febca728f93de")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
