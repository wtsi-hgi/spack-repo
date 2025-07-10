# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiochail(RPackage):
	"""basilisk and hail

	Use hail via basilisk when appropriate, or via reticulate. This package can be used in terra.bio to interact with UK Biobank resources processed by hail.is.
	"""
	
	homepage = "https://github.com/vjcitn/BiocHail"
	bioc = "BiocHail" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocHail_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocHail/BiocHail_1.2.0.tar.gz"]

	version("1.2.0", sha256="d56801f227b645e29814530e326c1820e35d5c78aaf6e4afa181f6bc3ad0ba09")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
