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

	version("0.99.2", commit="8df27c4e8c8fb85c65bf8e7722396f3cb44dc0ba")
	version("0.99.2", commit="8df27c4e8c8fb85c65bf8e7722396f3cb44dc0ba")

	depends_on("r@4.1:", type=("build", "run"))

