# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarr(RPackage):
	"""Read Zarr Files in R

	The Zarr specification defines a format for chunked, compressed, N-dimensional arrays.  It's design allows efficient access to subsets of the stored array, and supports both local and cloud storage systems. Rarr aims to implement this specifcation in R with minimal reliance on an external tools or libraries.
	"""
	
	homepage = "https://github.com/grimbough/Rarr"
	bioc = "Rarr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rarr_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rarr/Rarr_1.2.0.tar.gz"]

	version("1.2.0", md5="94af864ae3de3557840993a429944ea2")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-paws-storage", type=("build", "run"))
