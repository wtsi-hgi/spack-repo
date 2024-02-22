# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifecontingencies(RPackage):
	"""Financial and Actuarial Mathematics for Life Contingencies

	Classes and methods that allow the user to manage life table,
    actuarial tables (also multiple decrements tables). Moreover, functions to easily
    perform demographic, financial and actuarial mathematics on life contingencies
    insurances calculations are contained therein. See Spedicato (2013)	<doi:10.18637/jss.v055.i10>.
	"""
	
	homepage = "https://github.com/spedygiorgio/lifecontingencies"
	cran = "lifecontingencies" 

	version("1.3.11", md5="e7237d3b7b47d1ccbccb7bd6f1007889")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-markovchain", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
