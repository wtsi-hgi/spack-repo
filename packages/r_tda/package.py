# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTda(RPackage):
	"""Statistical Tools for Topological Data Analysis

	Tools for the statistical analysis of persistent homology and for
    density clustering. For that, this package provides an R interface for the
    efficient algorithms of the C++ libraries 'GUDHI' <https://project.inria.fr/gudhi/software/>, 'Dionysus' <https://www.mrzv.org/software/dionysus/>, and 'PHAT' <https://bitbucket.org/phat-code/phat/>. This package also implements the methods in Fasy et al. (2014) <doi:10.1214/14-AOS1252> and Chazal et al. (2014) <doi:10.1145/2582112.2582128>  for analyzing the statistical significance of persistent homology features.
	"""
	
	cran = "TDA" 

	version("1.9.1", md5="0f6b691c12c28e35acdb49293c3f6495")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-bh@1.81.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
