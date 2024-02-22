# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadGt3x(RPackage):
	"""Parse 'ActiGraph' 'GT3X'/'GT3X+' 'Accelerometer' Data

	Implements a high performance C++ parser 
    for 'ActiGraph' 'GT3X'/'GT3X+' data format (with extension '.gt3x') 
    for 'accelerometer' samples. Activity samples can be easily read into a
    matrix or data.frame.  This allows for storing the raw 'accelerometer' 
    samples in the original binary format to reserve space.
	"""
	
	cran = "read.gt3x" 

	version("1.2.0", md5="cf048c444e67b932db8db87af877fb1c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
