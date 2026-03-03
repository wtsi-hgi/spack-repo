# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistcomp(RPackage):
	"""Computations over Distributed Data without Aggregation

	Implementing algorithms and fitting models when sites (possibly remote) share
  computation summaries rather than actual data over HTTP with a master R process (using
  'opencpu', for example). A stratified Cox model and a singular value decomposition are
  provided. The former makes direct use of code from the R 'survival' package. (That is,
  the underlying Cox model code is derived from that in the R 'survival' package.)
  Sites may provide data via several means: CSV files, Redcap API, etc. An extensible
  design allows for new methods to be added in the future and includes facilities
  for local prototyping and testing. Web applications are provided (via 'shiny') for
  the implemented methods to help in designing and deploying the computations.
	"""
	
	homepage = "http://dx.doi.org/10.18637/jss.v077.i13"
	cran = "distcomp" 

	version("1.3-3", md5="3c78430af2fe2b6284bda860d434e16f")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-homomorpher", type=("build", "run"))
	depends_on("r-gmp", type=("build", "run"))
