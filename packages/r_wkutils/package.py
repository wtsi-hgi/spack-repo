# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWkutils(RPackage):
	"""Utilities for Well-Known Geometry Vectors

	Provides extra utilities for well-known formats in the
  'wk' package that are outside the scope of that package. Utilities
  to parse coordinates from data frames, plot well-known geometry
  vectors, extract meta information from well-known geometry vectors,
  and calculate bounding boxes are provided.
	"""
	
	homepage = "https://paleolimbot.github.io/wkutils/"
	cran = "wkutils" 

	version("0.1.3", md5="dc407ae9dff24e92e3b86bd4e1b65912")

	depends_on("r-wk@0.3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
