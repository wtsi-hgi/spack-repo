# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiHelpers(RPackage):
	"""'rbi' Helper Functions

	Contains a collection of helper functions to use with 'rbi', the R
  interface to 'LibBi', described in
  Murray et al. (2015) <doi:10.18637/jss.v067.i10>. It contains functions to
  adapt the proposal distribution and number of particles in
  particle Markov-Chain Monte Carlo, as well as calculating the
  Deviance Information Criterion (DIC) and converting between times in 'LibBi'
  results and R time/dates.
	"""
	
	homepage = "https://libbi.org"
	cran = "rbi.helpers" 

	version("0.4.0", md5="6c2fd2b745f3e9ff70066cb692d42759")

	depends_on("r-rbi@0.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
