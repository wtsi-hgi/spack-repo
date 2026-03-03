# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR6extended(RPackage):
	"""Extension for 'R6' Base Class

	Useful methods and data fields to extend the
             bare bones 'R6' class provided by the 'R6' package - ls-method, 
             hashes, warning- and message-method, general get-method and a 
             debug-method that assigns self and private to the global environment.
	"""
	
	homepage = "https://github.com/petermeissner/r6extended"
	cran = "r6extended" 

	version("0.1.2", md5="74ea50ff7d1e8d22adc4f4e2b6c6d2af")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6@2.2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-digest@0.6.12:", type=("build", "run"))
	depends_on("r-hellno@0.0.1:", type=("build", "run"))
