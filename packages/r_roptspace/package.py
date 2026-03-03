# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoptspace(RPackage):
	"""Matrix Reconstruction from a Few Entries

	Matrix reconstruction, also known as matrix completion, is the task of inferring missing entries of a partially observed matrix. This package provides a method called OptSpace, which was proposed by Keshavan, R.H., Oh, S., and Montanari, A. (2009) <doi:10.1109/ISIT.2009.5205567> for a case under low-rank assumption.
	"""
	
	cran = "ROptSpace" 

	version("0.2.3", md5="0725b9f4bda3d3d1e8656ede588b32e7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
