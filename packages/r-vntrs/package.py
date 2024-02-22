# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVntrs(RPackage):
	"""Variable Neighborhood Trust Region Search

	An implementation of the variable neighborhood trust region 
    algorithm Bierlaire et al. (2009) "A Heuristic for Nonlinear Global 
    Optimization" <doi:10.1287/ijoc.1090.0343>. 
	"""
	
	homepage = "https://loelschlaeger.de/vntrs/"
	cran = "vntrs" 

	version("0.1.1", md5="248dd9256d7c150b1dace368faa6826e")

	depends_on("r-trust", type=("build", "run"))
