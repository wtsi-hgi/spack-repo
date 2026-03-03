# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlifo(RPackage):
	"""Don't Get Stuck with Stacks in R

	Functions to create and manipulate 
    FIFO (First In First Out), LIFO (Last In First Out), and NINO (Not In or Never Out) 
    stacks in R.
	"""
	
	homepage = "https://github.com/paulponcet/flifo"
	cran = "flifo" 

	version("0.1.5", md5="785ea5170fbb932c6d8c2655ec52b553")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-bazar", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
