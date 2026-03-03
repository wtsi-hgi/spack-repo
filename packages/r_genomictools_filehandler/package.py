# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenomictoolsFilehandler(RPackage):
	"""File Handlers for Genomic Data Analysis

	A collection of I/O tools for handling the most commonly used genomic datafiles, like fasta/-q, bed, gff, gtf, ped/map and vcf.
	"""
	
	cran = "GenomicTools.fileHandler" 

	version("0.1.5.9", md5="96b605a9429a98e8a349e46efc595dea")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
