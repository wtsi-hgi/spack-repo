# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsRn5(RPackage):
	"""RnBeads.rn5

	Automatically generated RnBeads annotation package for the assembly rn5.
	"""
	
	bioc = "RnBeads.rn5" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.rn5_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RnBeads.rn5/RnBeads.rn5_1.34.0.tar.gz"]

	version("1.34.0", md5="ed075717da62b68e7a9b47a14ac09a35", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RnBeads.rn5_1.34.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))

	# experiment