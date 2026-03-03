# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlothmm(RPackage):
	"""Plot Hidden Markov Models

	Hidden Markov Models are useful for modeling
 sequential data. This package provides several functions
 implemented in C++ for explaining the algorithms used for
 Hidden Markov Models (forward, backward, decoding,
 learning).
	"""
	
	cran = "plotHMM" 

	version("2023.8.28", md5="bc2ece62434296cc736f9078eea0a796")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
