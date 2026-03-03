# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsHg19(RPackage):
	"""RnBeads.hg19

	Automatically generated RnBeads annotation package for the assembly hg19.
	"""
	
	bioc = "RnBeads.hg19" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg19_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.hg19/RnBeads.hg19_1.34.0.tar.gz"]

	version("1.34.0", md5="92612251679ba9c6d2b88b90838edf1c", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.hg19_1.34.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

