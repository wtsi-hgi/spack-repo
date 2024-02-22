# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViscomplexr(RPackage):
	"""Phase Portraits of Functions in the Complex Number Plane

	Functionality for creating phase portraits of functions in the
    complex number plane. Works with R base graphics, whose full 
    functionality is available. Parallel processing is used for optimum 
    performance.
	"""
	
	homepage = "https://peterbiber.github.io/viscomplexr/"
	cran = "viscomplexr" 

	version("1.1.1", md5="0f0af3e245a4ae36005401101a0a017c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.15:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
