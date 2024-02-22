# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJti(RPackage):
	"""Junction Tree Inference

	Minimal and memory efficient implementation of the junction tree
	     algorithm using the Lauritzen-Spiegelhalter scheme;
	     S. L. Lauritzen and D. J. Spiegelhalter (1988) 
	     <https://www.jstor.org/stable/2345762?seq=1>.
	"""
	
	homepage = "https://github.com/mlindsk/jti"
	cran = "jti" 

	version("0.8.4", md5="d09685d15ac9f5e8d0dd8c06a04a4cd1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sparta", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
