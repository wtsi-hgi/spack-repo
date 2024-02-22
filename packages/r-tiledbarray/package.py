# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTiledbarray(RPackage):
	"""Using TileDB as a DelayedArray Backend

	Implements a DelayedArray backend for reading and writing dense or sparse arrays in the TileDB format. The resulting TileDBArrays are compatible with all Bioconductor pipelines that can accept DelayedArray instances.
	"""
	
	homepage = "https://github.com/LTLA/TileDBArray"
	bioc = "TileDBArray" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/TileDBArray_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/TileDBArray/TileDBArray_1.12.0.tar.gz"]

	version("1.12.0", md5="7bb6ef67d882031ac2ebfcb3c1873dd2")

	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tiledb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
