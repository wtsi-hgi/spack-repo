# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsingsampler(RPackage):
	"""Sampling Methods and Distribution Functions for the Ising Model

	Sample states from the Ising model and compute the probability of states. Sampling can be done for any number of nodes, but due to the intractibility of the Ising model the distribution can only be computed up to ~10 nodes.
	"""
	
	homepage = "github.com/SachaEpskamp/IsingSampler"
	cran = "IsingSampler" 

	version("0.2.3", md5="72797dd94ba0ba055e5ab081ffe74ebb")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
