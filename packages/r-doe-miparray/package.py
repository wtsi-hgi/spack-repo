# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoeMiparray(RPackage):
	"""Creation of Arrays by Mixed Integer Programming

	'CRAN' packages 'DoE.base' and 'Rmosek' and non-'CRAN' package 'gurobi' are enhanced with functionality for the creation of optimized arrays for experimentation, where optimization is in terms of generalized minimum aberration. It is also possible to optimally extend existing arrays to larger run size. The package writes 'MPS' (Mathematical Programming System) files for use with any mixed integer optimization software that can process such files. If at least one of the commercial products 'Gurobi' or 'Mosek' (free academic licenses available for both) is available, the package also creates arrays by optimization. For installing 'Gurobi' and its R package 'gurobi', follow instructions at <https://www.gurobi.com/products/gurobi-optimizer/> and <https://www.gurobi.com/documentation/7.5/refman/r_api_overview.html> (or higher version). For installing 'Mosek' and its R package 'Rmosek', follow instructions at <https://www.mosek.com/downloads/> and <https://docs.mosek.com/8.1/rmosek/install-interface.html>, or use the functionality in the stump CRAN R package 'Rmosek'.
	"""
	
	cran = "DoE.MIParray" 

	version("1.0-1", md5="bceb8ae824a354320563033340bf1a26")

	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-doe-base", type=("build", "run"))
