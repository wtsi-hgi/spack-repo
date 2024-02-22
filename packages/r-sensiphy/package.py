# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensiphy(RPackage):
	"""Sensitivity Analysis for Comparative Methods

	An implementation of sensitivity analysis for phylogenetic comparative
 methods. The package is an umbrella of statistical and graphical methods that 
 estimate and report different types of uncertainty in PCM:
 (i) Species Sampling uncertainty (sample size; influential species and clades).
 (ii) Phylogenetic uncertainty (different topologies and/or branch lengths).
 (iii) Data uncertainty (intraspecific variation and measurement error).
	"""
	
	homepage = "https://github.com/paternogbc/sensiPhy"
	cran = "sensiPhy" 

	version("0.8.5", md5="6cfa41f5806c429354d410af7022b875")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ape@3.3:", type=("build", "run"))
	depends_on("r-phylolm@2.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-caper@0.5.2:", type=("build", "run"))
	depends_on("r-phytools@0.6:", type=("build", "run"))
	depends_on("r-geiger@2:", type=("build", "run"))
