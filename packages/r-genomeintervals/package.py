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

    version("1.64.0", tag="RELEASE_3_21")
	version("1.58.0", sha256="1915392190e53c5028c90a0d5b3d11637bef0c3f6ddf79581a7233bde6282d09")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-intervals@0.14:", type=("build", "run"))
	depends_on("r-biocgenerics@0.15.2:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.5.8:", type=("build", "run"))
	depends_on("r-genomicranges@1.21.16:", type=("build", "run"))
	depends_on("r-iranges@2.3.14:", type=("build", "run"))
	depends_on("r-s4vectors@0.7.10:", type=("build", "run"))
