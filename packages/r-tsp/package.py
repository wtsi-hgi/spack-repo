# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsp(RPackage):
	"""Traveling Salesperson Problem (TSP)

	Basic infrastructure and some algorithms for the traveling
    salesperson problem (also traveling salesman problem; TSP).
    The package provides some simple algorithms and
    an interface to the Concorde TSP solver and its implementation of the
    Chained-Lin-Kernighan heuristic. The code for Concorde
    itself is not included in the package and has to be obtained separately.
    Hahsler and Hornik (2007) <doi:10.18637/jss.v023.i02>.
	"""
	
	homepage = "https://github.com/mhahsler/TSP"
	cran = "TSP" 

	version("1.2-4", md5="118b45608aabf22def700a73a04a1e90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))

