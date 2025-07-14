# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdAtdschipTiling(RPackage):
	"""Platform Design Info for Affymetrix Atdschip_tiling

	Platform Design Info for Affymetrix Atdschip_tiling
	"""
	
	bioc = "pd.atdschip.tiling" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/pd.atdschip.tiling_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/pd.atdschip.tiling/pd.atdschip.tiling_0.40.0.tar.gz"]

    version("0.46.0", tag="RELEASE_3_21")
	version("0.40.0", sha256="dc389eaee4017c5facbe34089f26aff0e09af559834fee3623d5d6467efadb0f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rsqlite@0.10:", type=("build", "run"))
	depends_on("r-oligoclasses@1.15.58:", type=("build", "run"))
	depends_on("r-oligo@1.17.3:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biostrings@2.21.11:", type=("build", "run"))
	depends_on("r-iranges@1.11.31:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

