# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalsolver(RPackage):
	"""R API to LocalSolver

	The package converts R data onto input and data for LocalSolver,
    executes optimization and exposes optimization results as R data.
    LocalSolver (http://www.localsolver.com/) is an optimization engine
    developed by Innovation24 (http://www.innovation24.fr/). It is designed to
    solve large-scale mixed-variable non-convex optimization problems.  The
    localsolver package is developed and maintained by WLOG Solutions
    (http://www.wlogsolutions.com/en/) in collaboration with Decision Support
    and Analysis Division at Warsaw School of Economics
    (http://www.sgh.waw.pl/en/).
	"""
	
	cran = "localsolver" 

	version("2.3", md5="49e55203356955f5c3c9782b4fc053c9")

	depends_on("r@3.0.1:", type=("build", "run"))
