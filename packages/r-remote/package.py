# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemote(RPackage):
	"""Empirical Orthogonal Teleconnections in R

	Empirical orthogonal teleconnections in R.
    'remote' is short for 'R(-based) EMpirical Orthogonal TEleconnections'.
    It implements a collection of functions to facilitate empirical
    orthogonal teleconnection analysis. Empirical Orthogonal Teleconnections
    (EOTs) denote a regression based approach to decompose spatio-temporal
    fields into a set of independent orthogonal patterns. They are quite
    similar to Empirical Orthogonal Functions (EOFs) with EOTs producing
    less abstract results. In contrast to EOFs, which are orthogonal in both
    space and time, EOT analysis produces patterns that are orthogonal in
    either space or time.
	"""
	
	cran = "remote" 

	version("1.2.1", md5="9b98807d815cca0e8ea61006fd0996db")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
