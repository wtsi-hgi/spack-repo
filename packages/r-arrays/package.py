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

	version("1.28.0", sha256="b120eca4c4cd349df064f7e37655f6294c4ca312019daff8b237a2e08b2331c3")

	depends_on("r@3:", type=("build", "run"))

