# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecmap(RPackage):
	"""Compute the Rectangular Statistical Cartogram

	Implements the RecMap MP2 construction heuristic
  <doi:10.1109/INFVIS.2004.57>.
  This algorithm draws maps according to a given statistical
  value, e.g., election results, population, or epidemiological data.
  The basic idea of the RecMap algorithm is that each map region,
  e.g., different countries, is represented by a rectangle.
  The area of each rectangle represents the statistical value given
  as input (maintain zero cartographic error).
  C++ is used to implement the computationally intensive tasks.
  The vignette included in this package provides documentation
  about the usage of the recmap algorithm.
	"""
	
	cran = "recmap" 

	version("1.0.17", md5="69281f1bdc88b1c75c31aee342948a0c")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ga@3.1:", type=("build", "run"))
	depends_on("r-rcpp@1:", type=("build", "run"))
	depends_on("r-sp@1.3:", type=("build", "run"))
