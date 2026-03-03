# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatata(RPackage):
	"""Create Constraints for Small Test Assembly Problems

	Provides simple functions to create constraints for small test assembly problems 
    (e.g. van der Linden (2005, ISBN: 978-0-387-29054-6)) using sparse matrices. Currently, 
    'GLPK', 'lpSolve', 'Symphony', and 'Gurobi' are supported as solvers. The 'gurobi' package is not available from 
    any mainstream repository; see <https://www.gurobi.com/downloads/>.
	"""
	
	homepage = "https://github.com/beckerbenj/eatATA"
	cran = "eatATA" 

	version("1.1.2", md5="87f0bbad6eb4c495d076586b2b7dc805")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
