# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRibor(RPackage):
	"""An R Interface for Ribo Files

	The ribor package provides an R Interface for .ribo files. It provides functionality to read the .ribo file, which is of HDF5 format, and performs common analyses on its contents.
	"""
	
	bioc = "ribor" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ribor_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ribor/ribor_1.14.0.tar.gz"]

	version("1.14.0", md5="6d86ac039324d8fa1b6c708f42da44e2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
