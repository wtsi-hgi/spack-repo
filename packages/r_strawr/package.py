# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrawr(RPackage):
	"""Fast Implementation of Reading/Dump for .hic Files

	API for fast data extraction for .hic files that provides programmatic access to the matrices. It doesn't store the pointer data for all the matrices, only the one queried, and currently we are only supporting matrices (not vectors).
	"""
	
	homepage = "https://github.com/aidenlab/straw/tree/master/R"
	cran = "strawr" 

	version("0.0.91", md5="9221016b47c870f5e626e2eec4fb572b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
