# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRotations(RPackage):
	"""Working with Rotation Data

	Tools for working with rotational data, including
    simulation from the most commonly used distributions on SO(3),
    methods for different Bayes, mean and median type estimators for
    the central orientation of a sample, confidence/credible
    regions for the central orientation based on those estimators and
    a novel visualization technique for rotation data.  Most recently,
    functions to identify potentially discordant (outlying) values
    have been added.  References: Bingham, Melissa A. and Nordman, Dan J. and Vardeman, Steve B. (2009),
    Bingham, Melissa A and Vardeman, Stephen B and Nordman, Daniel J (2009),
    Bingham, Melissa A and Nordman, Daniel J and Vardeman, Stephen B (2010),
    Leon, C.A. and Masse, J.C. and Rivest, L.P. (2006),
    Hartley, R and Aftab, K and Trumpf, J. (2011),
    Stanfill, Bryan and Genschel, Ulrike and Hofmann, Heike (2013),
    Maonton, Jonathan (2004), 
    Mardia, KV and Jupp, PE (2000, ISBN:9780471953333), 
    Rancourt, D. and Rivest, L.P. and Asselin, J. (2000),
    Chang, Ted and Rivest, Louis-Paul (2001), 
    Fisher, Nicholas I. (1996, ISBN:0521568900).
	"""
	
	homepage = "https://github.com/stanfill/rotationsC"
	cran = "rotations" 

	version("1.6.5", md5="3351681ae67b634ac6998ea9e0108ee9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
