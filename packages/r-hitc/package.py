# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHitc(RPackage):
	"""High Throughput Chromosome Conformation Capture analysis

	The HiTC package was developed to explore high-throughput 'C' data such as 5C or Hi-C. Dedicated R classes as well as standard methods for quality controls, normalization, visualization, and further analysis are also provided.
	"""
	
	bioc = "HiTC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/HiTC_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/HiTC/HiTC_1.46.0.tar.gz"]

	version("1.46.0", md5="e530516c0386e2e9bb6ff9afbed5893f")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
