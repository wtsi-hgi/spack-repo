# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiobtreer(RPackage):
	"""Using biobtree tool from R

	The biobtreeR package provides an interface to [biobtree](https://github.com/tamerh/biobtree) tool which covers large set of bioinformatics datasets and allows search and chain mappings functionalities.
	"""
	
	homepage = "https://github.com/tamerh/biobtreeR"
	bioc = "biobtreeR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biobtreeR_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biobtreeR/biobtreeR_1.14.0.tar.gz"]

	version("1.20.0", tag="RELEASE_3_21")
	version("1.14.0", sha256="e5a0e9dbff233fdd9c4b88c192155c0d524991c1e6c83c7be788cf7b8fc9e5a2")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
