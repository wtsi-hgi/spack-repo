# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWes1kgWugsc(RPackage):
	"""Whole Exome Sequencing (WES) of chromosome 22 401st to 500th exon from the 1000 Genomes (1KG) Project by the Washington University Genome Sequencing Center (WUGSC).

	The assembled .bam files of whole exome sequencing data from the 1000 Genomes Project. 46 samples sequenced by the Washington University Genome Sequencing Center are included.
	"""
	
	bioc = "WES.1KG.WUGSC"

	version("1.40.0", commit="2a03e4e2108d3f10826fd5f079e658011f757c93")
	version("1.34.0", commit="5add20b7572f98290185d654865604932d3f6f4c")


