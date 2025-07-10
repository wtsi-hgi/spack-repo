# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtopper(RPackage):
	"""This package is designed to perform Gene Set Analysis across multiple genomic platforms

	the RTopper package is designed to perform and integrate gene set enrichment results across multiple genomic platforms.
	"""
	
	bioc = "RTopper" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RTopper_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RTopper/RTopper_1.48.0.tar.gz"]

	version("1.48.0", sha256="a6ab357c6469ad1ae52e178287ae71106923cc044dc29292310d0bf527eb594a")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
