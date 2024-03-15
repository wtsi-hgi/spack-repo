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

	version("0.99.2", md5="eec85c20139b3d826f00264c7b28207c")

	depends_on("r@4.1:", type=("build", "run"))

	# annotation