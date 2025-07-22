# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromhmmdata(RPackage):
	"""Chromosome Size, Coordinates and Anchor Files

	Annotation files of the formatted genomic annotation for ChromHMM. Three types of text files are included the chromosome sizes, region coordinates and anchors specifying the transcription start and end sites. The package includes data for two versions of the genome of humans and mice.
	"""
	
	bioc = "chromhmmData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/chromhmmData_0.99.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/chromhmmData/chromhmmData_0.99.2.tar.gz"]

	version("0.99.2", tag="RELEASE_3_21")
	version("0.99.2", sha256="f23b04ecd03c29a7fbf1c01f461101f9d1f8f443fa9aeccfc6e9cffae9e9e68d")

	depends_on("r@4.1:", type=("build", "run"))

