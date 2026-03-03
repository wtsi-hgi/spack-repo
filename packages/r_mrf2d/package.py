# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrf2d(RPackage):
	"""Markov Random Field Models for Image Analysis

	Model fitting, sampling and visualization
    for the (Hidden) Markov Random Field model with pairwise interactions and 
    general interaction structure from 
    Freguglia, Garcia & Bicas (2020) <doi:10.1002/env.2613>,
    which has many popular models used in 2-dimensional lattices
    as particular cases, like the Ising Model and Potts Model.
    A complete manuscript describing the package is available in
    Freguglia & Garcia (2022) <doi:10.18637/jss.v101.i08>.
	"""
	
	homepage = "https://github.com/Freguglia/mrf2d"
	cran = "mrf2d" 

	version("1.0", md5="66afbcc29f0b1e1c63198e1c37b940c6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
