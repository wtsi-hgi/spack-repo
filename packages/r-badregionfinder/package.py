# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBadregionfinder(RPackage):
	"""BadRegionFinder: an R/Bioconductor package for identifying regions with bad coverage

	BadRegionFinder is a package for identifying regions with a bad, acceptable and good coverage in sequence alignment data available as bam files. The whole genome may be considered as well as a set of target regions. Various visual and textual types of output are available.
	"""
	
	bioc = "BadRegionFinder" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BadRegionFinder_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BadRegionFinder/BadRegionFinder_1.30.0.tar.gz"]

	version("1.30.0", sha256="899e1a53005b78e9a98435143c2fd835b71429aec474c98c3dc66844e1a3559f")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
