# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabinr(RPackage):
	"""Abundance and Compositional Based Binning of Metagenomes

	Provide functions for performing abundance and compositional based binning on metagenomic samples, directly from FASTA or FASTQ files. Functions are implemented in Java and called via rJava. Parallel implementation that operates directly on input FASTA/FASTQ files for fast execution.
	"""
	
	homepage = "https://github.com/gkanogiannis/metabinR"
	bioc = "metabinR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/metabinR_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/metabinR/metabinR_1.4.0.tar.gz"]

	version("1.4.0", md5="7080ae8eac49640aeae95bda1185ac7d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
