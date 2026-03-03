# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2admb(RPackage):
	"""'ADMB' to R Interface Functions

	A series of functions to call 'AD Model Builder' (i.e.,
    compile and run models) from within R, read the results back
    into R as 'admb' objects, and provide standard accessors (i.e.
    coef(), vcov(), etc.)
	"""
	
	cran = "R2admb" 

	version("0.7.16.3", md5="0d434481a78a89fb6873d54c205b87ca")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
