# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocbaseutils(RPackage):
	"""General utility functions for developing Bioconductor packages

	The package provides utility functions related to package development. These include functions that replace slots, and selectors for show methods. It aims to coalesce the various helper functions often re-used throughout the Bioconductor ecosystem.
	"""
	
	bioc = "BiocBaseUtils" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocBaseUtils_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocBaseUtils/BiocBaseUtils_1.4.0.tar.gz"]

	version("1.4.0", md5="23ed1406ff70165a763ca2040c46353e")

	depends_on("r@4.2:", type=("build", "run"))
