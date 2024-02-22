# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTodor(RPackage):
	"""Find All TODO Comments and More

	This is a simple addin to 'RStudio' that finds all 'TODO', 'FIX ME', 'CHANGED' etc. comments in your project and shows them as a markers list.
	"""
	
	cran = "todor" 

	version("0.1.2", md5="0934e4acc5dea4aceceb08b9bfe6bf04")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
