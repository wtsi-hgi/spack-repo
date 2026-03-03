# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRMatlab(RPackage):
	"""Read and Write MAT Files and Call MATLAB from Within R

	Methods readMat() and writeMat() for reading and writing MAT files.  For user with MATLAB v6 or newer installed (either locally or on a remote host), the package also provides methods for controlling MATLAB (trademark) via R and sending and retrieving data between R and MATLAB.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/R.matlab"
	cran = "R.matlab" 

	version("3.7.0", md5="97bbf20777db9348e31aae160a761c03")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-r-methodss3@1.7.1:", type=("build", "run"))
	depends_on("r-r-oo@1.23:", type=("build", "run"))
	depends_on("r-r-utils@2.5:", type=("build", "run"))
