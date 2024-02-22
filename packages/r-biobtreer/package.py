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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/biobtreeR_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/biobtreeR/biobtreeR_1.14.0.tar.gz"]

	version("1.14.0", md5="c341e537e79161abfd6f1f3382d3eb90")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
