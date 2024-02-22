# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdts(RPackage):
	"""Detection of de novo deletion in targeted sequencing trios

	A package for the detection of de novo copy number deletions in targeted sequencing of trios with high sensitivity and positive predictive value.
	"""
	
	bioc = "MDTS" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MDTS_1.22.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MDTS/MDTS_1.22.0.tar.gz"]

	version("1.22.0", md5="a9ab8fa7a5e9ef7dcdb28fb553b895f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
