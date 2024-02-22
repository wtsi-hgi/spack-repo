# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqminer(RPackage):
	"""Efficiently Read Sequence Data (VCF Format, BCF Format, METAL
Format and BGEN Format) into R

	Integrate sequencing data (Variant call format, e.g. VCF or BCF) or meta-analysis results in R. This package can help you (1) read VCF/BCF/BGEN files by chromosomal ranges (e.g. 1:100-200); (2) read RareMETAL summary statistics files; (3) read tables from a tabix-indexed files; (4) annotate VCF/BCF files; (5) create customized workflow based on Makefile.
	"""
	
	homepage = "http://zhanxw.github.io/seqminer/"
	cran = "seqminer" 

	version("9.4", md5="5922d7a82037e970121b8b31df2c53cc")

	depends_on("zlib", type=("build", "link", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
