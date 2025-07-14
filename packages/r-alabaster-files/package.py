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

	version("1.6.0", commit="c7480ac77d3c61e7f05a8780f79d559f3f4cc6ca")
	version("1.0.0", commit="7ed94414fafca70f281e9fa709e9a53699f825cc")

	depends_on("r-alabaster-base", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
