# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsrank(RPackage):
	"""Compute the Median Ranking(s) According to the Kemeny's
Axiomatic Approach

	Compute the median ranking according to the Kemeny's axiomatic approach. 
    Rankings can or cannot contain ties, rankings can be both complete or incomplete. 
    The package contains both branch-and-bound algorithms and heuristic solutions recently proposed. 
    The searching space of the solution can either be restricted to the universe of the permutations or unrestricted to all possible ties. 
    The package also provide some useful utilities for deal with preference rankings, including both element-weight Kemeny distance and correlation coefficient.
    This release declare as deprecated some functions that are still in the package for compatibility. Next release will not contains these functions.
    Please type '?ConsRank-deprecated'
    Essential references:
    Emond, E.J., and Mason, D.W. (2002) <doi:10.1002/mcda.313>; 
    D'Ambrosio, A., Amodio, S., and Iorio, C. (2015) <doi:10.1285/i20705948v8n2p198>; 
    Amodio, S., D'Ambrosio, A., and Siciliano R. (2016) <doi:10.1016/j.ejor.2015.08.048>; 
    D'Ambrosio, A., Mazzeo, G., Iorio, C., and Siciliano, R. (2017) <doi:10.1016/j.cor.2017.01.017>;
    Albano, A., and Plaia, A. (2021) <doi:10.1285/i20705948v14n1p117>.
	"""
	
	homepage = "https://www.r-project.org/"
	cran = "ConsRank" 

	version("2.1.4", md5="eaa7f5278805dd3564a6bd4ed414fcc9")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-rlist@0.4.2:", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
