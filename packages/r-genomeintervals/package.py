# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomeintervals(RPackage):
	"""Operations on genomic intervals

	This package defines classes for representing genomic intervals and provides functions and methods for working with these. Note: The package provides the basic infrastructure for and is enhanced by the package 'girafe'.
	"""
	
	bioc = "genomeIntervals" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/genomeIntervals_1.58.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/genomeIntervals/genomeIntervals_1.58.0.tar.gz"]

	version("1.58.0", md5="c47b9bb1293b799a7ac75fef82f45589")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-intervals@0.14:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.2:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.5.8:", type=("build", "run"))
	depends_on("r-genomicranges@1.21.16:", type=("build", "run"))
	depends_on("r-iranges@2.3.14:", type=("build", "run"))
	depends_on("r-s4vectors@0.7.10:", type=("build", "run"))
