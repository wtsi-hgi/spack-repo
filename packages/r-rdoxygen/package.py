# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdoxygen(RPackage):
	"""Create Doxygen Documentation for Source Code

	Create doxygen documentation for source code in R packages. 
  Includes a RStudio Addin, that allows to trigger the doxygenize process.
	"""
	
	homepage = "https://github.com/nevrome/rdoxygen"
	cran = "rdoxygen" 

	version("1.0.0", md5="418977feb51198124cf5d3663d2a99da")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-devtools@1.12:", type=("build", "run"))
	depends_on("doxygen", type=("build", "link", "run"))
