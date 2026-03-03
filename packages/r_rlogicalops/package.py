# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlogicalops(RPackage):
	"""Process Logical Operations

	Processing logical operations such as AND/OR/NOT operations
    dynamically. It also handles nesting in the operations.
	"""
	
	cran = "RLogicalOps" 

	version("0.1", md5="6dd54482cfb6a9afe2b0b12b036eacf5")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rstackdeque", type=("build", "run"))
