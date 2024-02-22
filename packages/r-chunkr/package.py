# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChunkr(RPackage):
	"""Read Tables in Chunks

	Read tables chunk by chunk using a C++ backend and a simple R interface.
	"""
	
	cran = "chunkR" 

	version("1.1.1", md5="0db605cb20b913c76bc2e72e29efd7e0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
