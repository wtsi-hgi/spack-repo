# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcdag(RPackage):
	"""Bayesian Structure and Causal Learning of Gaussian Directed
Graphs

	A collection of functions for structure learning of causal networks and estimation of joint causal effects from observational Gaussian data. Main algorithm consists of a Markov chain Monte Carlo scheme for posterior inference of causal structures, parameters and causal effects between variables.
    References:
    F. Castelletti and A. Mascaro (2021) <doi:10.1007/s10260-021-00579-1>,
    F. Castelletti and A. Mascaro (2022) <arXiv:2201.12003>.
	"""
	
	homepage = "https://github.com/alesmascaro/BCDAG"
	cran = "BCDAG" 

	version("1.1.0", md5="256d07b424348f682f8d6eaf821cea36")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
