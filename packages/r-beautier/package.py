# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeautier(RPackage):
	"""'BEAUti' from R

	'BEAST2' (<https://www.beast2.org>) is a widely used
  Bayesian phylogenetic tool, that uses DNA/RNA/protein data
  and many model priors to create a posterior of jointly estimated 
  phylogenies and parameters.
  'BEAUti 2' (which is part of 'BEAST2') is a GUI tool 
  that allows users to specify the many possible setups
  and generates the XML file 'BEAST2' needs to run.
  This package provides a way to create 'BEAST2' input
  files without active user input, but using
  R function calls instead.
	"""
	
	homepage = "https://docs.ropensci.org/beautier/"
	cran = "beautier" 

	version("2.6.11", md5="c35bf69e01443fa9720556ce93989536")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
