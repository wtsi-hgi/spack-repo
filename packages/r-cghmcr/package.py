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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cghMCR_1.60.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cghMCR/cghMCR_1.60.0.tar.gz"]

	version("1.60.0", md5="b3db4bfc3f23e690592a37414db360c9")

	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-cntools", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
