# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrays(RPackage):
	"""Using Bioconductor for Microarray Analysis

	Using Bioconductor for Microarray Analysis workflow
	"""
	
	bioc = "arrays" 
	urls = ["https://www.bioconductor.org/packages/3.18/workflows/src/contrib/arrays_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/workflows/src/contrib/Archive/arrays/arrays_1.28.0.tar.gz"]

	version("1.28.0", md5="466fc4abd4aea25b91a224839b146532")

	depends_on("r@3:", type=("build", "run"))

	# workflow