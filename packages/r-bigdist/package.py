# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigdist(RPackage):
	"""Store Distance Matrices on Disk

	Provides utilities to compute, store and access distance matrices on disk as file-backed matrices provided by the 'bigstatsr' package. File-backed distance matrices are stored as a symmetric matrix to facilitate out-of-memory operations on file-backed matrix while the in-memory 'dist' object stores only the lower diagonal elements. 'disto' provides an unified interface to work with in-memory and disk-based distance matrices.
	"""
	
	homepage = "https://github.com/talegari/bigdist"
	cran = "bigdist" 

	version("0.1.4", md5="e8c4439d27aae684fdcfe5c53a021615")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-bigstatsr@0.9.1:", type=("build", "run"))
	depends_on("r-proxy@0.4.21:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
