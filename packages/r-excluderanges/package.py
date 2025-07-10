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
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/excluderanges_0.99.8.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/excluderanges/excluderanges_0.99.8.tar.gz"]

	version("0.99.8", sha256="c261c494ca3e03440bb86f9344f391b89c640bc6655cefba4ccc9183f3a731b2")

	depends_on("r-genomicranges", type=("build", "run"))

