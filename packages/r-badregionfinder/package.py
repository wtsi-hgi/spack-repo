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

	version("1.30.0", md5="c492af1d6b1297cd322a79355e3d3664")

	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
