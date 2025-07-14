# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromstardata(RPackage):
	"""ChIP-seq data for Demonstration Purposes

	ChIP-seq data for demonstration purposes in the chromstaR package.
	"""
	
	bioc = "chromstaRData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/chromstaRData_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/chromstaRData/chromstaRData_1.28.0.tar.gz"]

    version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="26eaddd6d147ac17327636cad136f4d964bedf05e0124cc281dabbdc536eb98f")

	depends_on("r@3.3:", type=("build", "run"))

