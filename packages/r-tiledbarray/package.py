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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TileDBArray_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TileDBArray/TileDBArray_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="920703cc68b3dbad43aaac626efb3d8a1e5c7f18fbdf95f9ade80ef878ada1d7")

	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tiledb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
