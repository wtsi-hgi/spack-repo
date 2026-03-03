# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenalgo(RPackage):
	"""Classes and Methods to Use Genetic Algorithms for Feature
Selection

	Defines classes and methods that can be used
  to implement genetic algorithms for feature selection.  The idea is
  that we want to select a fixed number of features to combine into a
  linear classifier that can predict a binary outcome, and can use a
  genetic algorithm heuristically to select an optimal set of features.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "GenAlgo" 

	version("2.2.0", md5="bb3d55c59bdebc9768c5a51ee9403a09")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-oompabase@3.0.1:", type=("build", "run"))
	depends_on("r-classdiscovery", type=("build", "run"))
