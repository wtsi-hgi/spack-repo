# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcluderanges(RPackage):
	"""Genomic coordinates of problematic genomic regions

	Genomic coordinates of problematic genomic regions that should be avoided when working with genomic data. GRanges of exclusion regions (formerly known as blacklisted), centromeres, telomeres, known heterochromatin regions, etc. (UCSC 'gap' table data). Primarily for human and mouse genomes, hg19/hg38 and mm9/mm10 genome assemblies.
	"""
	
	homepage = "https://github.com/dozmorovlab/excluderanges"
	bioc = "excluderanges" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/excluderanges_0.99.8.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/excluderanges/excluderanges_0.99.8.tar.gz"]

	version("0.99.8", md5="2ec19df8a51df1900a339f7f505cd5fa")

	depends_on("r-genomicranges", type=("build", "run"))

	# annotation