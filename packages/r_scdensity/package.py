# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdensity(RPackage):
	"""Shape-Constrained Kernel Density Estimation

	Implements methods for obtaining kernel density estimates
    subject to a variety of shape constraints (unimodality, bimodality, 
    symmetry, tail monotonicity, bounds, and constraints on the number of 
    inflection points). Enforcing constraints can eliminate unwanted waves or 
    kinks in the estimate, which improves its subjective appearance and can 
    also improve statistical performance. The main function scdensity() is 
    very similar to the density() function in 'stats', allowing 
    shape-restricted estimates to be obtained with little effort. The 
    methods implemented in this package are described in Wolters and Braun 
    (2017) <doi:10.1080/03610918.2017.1288247>, Wolters (2012) 
    <doi:10.18637/jss.v047.i06>, and Hall and Huang (2002) 
    <http://www3.stat.sinica.edu.tw/statistica/j12n4/j12n41/j12n41.htm>.  
    See the scdensity() help for for full citations.
	"""
	
	cran = "scdensity" 

	version("1.0.2", md5="6e19dc31673b577eb08579420fe3ac00")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
