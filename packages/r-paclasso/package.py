# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaclasso(RPackage):
	"""Penalized and Constrained Lasso Optimization

	An implementation of both the equality and inequality constrained lasso
    functions for the algorithm described in "Penalized and Constrained Optimization"
    by James, Paulson, and Rusmevichientong (Journal of the American Statistical Association, 2019;
    see <http://www-bcf.usc.edu/~gareth/research/PAC.pdf> for a full-text version of the paper). 
    The algorithm here is designed to allow users to define linear constraints (either equality
    or inequality constraints) and use a penalized regression approach to solve the constrained
    problem. The functions here are used specifically for constraints with the lasso formulation,
    but the method described in the PaC paper can be used for a variety of scenarios. In addition
    to the simple examples included here with the corresponding functions, complete code to 
    entirely reproduce the results of the paper is available online through the Journal of the
    American Statistical Association. 
	"""
	
	homepage = "http://www-bcf.usc.edu/~gareth/research/PAC.pdf"
	cran = "PACLasso" 

	version("1.0.0", md5="7fd9e79b4c1cf250da55a889c4e4d544")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-penalized@0.9:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-lars@1.2:", type=("build", "run"))
	depends_on("r-quadprog@1.5:", type=("build", "run"))
	depends_on("r-limsolve@1.5.5.3:", type=("build", "run"))
