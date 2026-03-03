# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastmatmr(RPackage):
	"""High-Performance Matrix Market File Operations

	An interface to the 'fast_matrix_market' 'C++' library, this package offers efficient read and write operations for Matrix Market files in R. It supports both sparse and dense matrix formats. Peer-reviewed at ROpenSci (<https://github.com/ropensci/software-review/issues/606>).
	"""
	
	homepage = "https://github.com/ropensci/fastMatMR"
	cran = "fastMatMR" 

	version("1.2.5", md5="6ab751e3403398b7828c613605fe9203")

	depends_on("r-cpp11", type=("build", "run"))
