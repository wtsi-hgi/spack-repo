# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcf(RPackage):
	"""Adapted Pair Correlation Function

	The adapted pair correlation function transfers the concept of the
  pair correlation function from point patterns to patterns of objects of
  finite size and irregular shape (e.g. lakes within a country).  The pair
  correlation function describes the spatial distribution of objects, e.g.
  random, aggregated or regularly spaced. This is a reimplementation of the
  method suggested by Nuske et al. (2009) <doi:10.1016/j.foreco.2009.09.050>
  using the library 'GEOS'. 
	"""
	
	homepage = "https://rnuske.github.io/apcf/"
	cran = "apcf"

	version("0.3.0", md5="b49f8ee302aad15303002837aedae73e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-wk@0.6:", type=("build", "run"))
	depends_on("geos@3.4:", type=("build", "link", "run"))
