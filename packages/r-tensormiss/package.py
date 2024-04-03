# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensormiss(RPackage):
	"""Handle Missing Tensor Data with C++ Integration

	To handle higher-order tensor data. See Kolda and Bader (2009) <doi:10.1137/07070111X> for details on tensor. While existing packages on tensor data extend the base 'array' class to some data classes, this package serves as an alternative resort to handle tensor only as 'array' class.
    Some functionalities related to missingness are also supported.
	"""
	
	cran = "tensorMiss" 

	version("0.1.1", md5="e50a09d77316b183d71b56e133896894")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
