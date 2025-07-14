# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterFiles(RPackage):
	"""Wrappers to Save Common File Formats

	Save common bioinformatics file formats within the alabaster framework. This includes BAM, BED, VCF, bigWig, bigBed, FASTQ, FASTA and so on. We save and load additional metadata for each file, and we support linkage between each file and its corresponding index.
	"""
	
	bioc = "alabaster.files" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster.files_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster.files/alabaster.files_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="52c451b6c1a5f827a791ee99f3367596569f39a117f4cd368536247b52c98a80")

	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
