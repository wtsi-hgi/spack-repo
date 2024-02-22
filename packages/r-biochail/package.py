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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/BiocHail_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/BiocHail/BiocHail_1.2.0.tar.gz"]

	version("1.2.0", md5="4707c299d0bb3b41001065a753d89f33")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-basilisk", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
