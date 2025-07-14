# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdfflow(RPackage):
	"""ncdfFlow: A package that provides HDF5 based storage for flow cytometry data.

	Provides HDF5 storage based methods and functions for manipulation of flow cytometry data.
	"""
	
	bioc = "ncdfFlow" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ncdfFlow_2.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ncdfFlow/ncdfFlow_2.48.0.tar.gz"]

    version("2.54.0", tag="RELEASE_3_21")
	version("2.48.0", sha256="40a55019a80bde5e65ea68162b3cc24ac87366ee2ac621f6433826b3517b3b7d")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-zlibbioc", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
