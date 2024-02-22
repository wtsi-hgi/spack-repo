# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopbayes(RPackage):
	"""Bayesian Model to Estimate Population Trends from Counts Series

	Infers the trends of one or several animal populations over time 
    from series of counts. It does so by accounting for count precision 
    (provided or inferred based on expert knowledge, e.g. guesstimates), 
    smoothing the population rate of increase over time, and accounting for the
    maximum demographic potential of species. Inference is carried out in a 
    Bayesian framework. This work is part of the FRB-CESAB working group
    AfroBioDrivers 
    <https://www.fondationbiodiversite.fr/en/the-frb-in-action/programs-and-projects/le-cesab/afrobiodrivers/>.
	"""
	
	homepage = "https://frbcesab.github.io/popbayes/"
	cran = "popbayes" 

	version("1.2.0", md5="fb0d28c09a5291e2355d77776237e331")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("jags@4.1:", type=("build", "link", "run"))
