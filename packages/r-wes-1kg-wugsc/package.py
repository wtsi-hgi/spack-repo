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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/WES.1KG.WUGSC_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/WES.1KG.WUGSC/WES.1KG.WUGSC_1.34.0.tar.gz"]

	version("1.34.0", sha256="545af75217502ede37421b2fa794a411d960d51b3eba88cea590d0a2c3251fdd")


