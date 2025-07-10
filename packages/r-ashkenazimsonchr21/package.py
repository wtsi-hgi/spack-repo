# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAshkenazimsonchr21(RPackage):
	"""Annotated variants on the chromosome 21, human genome 19, Ashkenazim Trio son sample

	SonVariantsChr21 is a dataset of annotated genomic variants coming from Complete Genomics whole genome sequencing. Data comes from GIAB project, Ashkenazim Trio, sample HG002 run 1. Both vcf and annotated data frame are provided.
	"""
	
	bioc = "AshkenazimSonChr21" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/AshkenazimSonChr21_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/AshkenazimSonChr21/AshkenazimSonChr21_1.32.0.tar.gz"]

	version("1.32.0", sha256="5dae3d05f92ce47c939b37533d871f62c90978614a98d58d327041b90c26367a", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/AshkenazimSonChr21_1.32.0.tar.gz")


