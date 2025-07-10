# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghmcr(RPackage):
	"""Find chromosome regions showing common gains/losses

	This package provides functions to identify genomic regions of interests based on segmented copy number data from multiple samples.
	"""
	
	bioc = "cghMCR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cghMCR_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cghMCR/cghMCR_1.60.0.tar.gz"]

	version("1.60.0", sha256="f99cb0d0e4337d6a5656b955c73c877e80fb2d49583b546928e748d59fa64b47")

	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-cntools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
