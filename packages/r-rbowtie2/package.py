# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbowtie2(RPackage):
	"""An R Wrapper for Bowtie2 and AdapterRemoval

	This package provides an R wrapper of the popular bowtie2 sequencing reads aligner and AdapterRemoval, a convenient tool for rapid adapter trimming, identification, and read merging. The package contains wrapper functions that allow for genome indexing and alignment to those indexes. The package also allows for the creation of .bam files via Rsamtools.
	"""
	
	bioc = "Rbowtie2" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbowtie2_2.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rbowtie2/Rbowtie2_2.8.0.tar.gz"]

    version("2.14.0", tag="RELEASE_3_21")
	version("2.8.0", sha256="fb81f3101e38d5622ddd37fe15757cf8be529c0d9263c2e30cf70867a6bea137", url="https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rbowtie2_2.8.0.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("samtools", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
