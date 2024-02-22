# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxmc(RPackage):
	"""Maximized Monte Carlo

	An implementation of the Monte Carlo techniques described in details by Dufour (2006) <doi:10.1016/j.jeconom.2005.06.007> and Dufour and Khalaf (2007) <doi:10.1002/9780470996249.ch24>. The two main features available are the Monte Carlo method with tie-breaker, mc(), for discrete statistics, and the Maximized Monte Carlo, mmc(), for statistics with nuisance parameters.
	"""
	
	homepage = "https://github.com/julienneves/MaxMC"
	cran = "MaxMC" 

	version("0.1.1", md5="14ab16b8bc3310f01baa78ce79c1ada2")

	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-pso", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-nmof", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
