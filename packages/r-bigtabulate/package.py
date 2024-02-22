# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigtabulate(RPackage):
	"""Table, Apply, and Split Functionality for Matrix and
'big.matrix' Objects

	Extend the bigmemory package with 'table', 'tapply', and 'split'
    support for 'big.matrix' objects. The functions may also be used with native R
    matrices for improving speed and memory-efficiency.
	"""
	
	homepage = "http://www.bigmemory.org"
	cran = "bigtabulate" 

	version("1.1.9", md5="87d94d47033d5773167cae3f48d02d9b")

	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-biganalytics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
