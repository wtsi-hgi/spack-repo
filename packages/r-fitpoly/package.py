# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitpoly(RPackage):
	"""Genotype Calling for Bi-Allelic Marker Assays

	Genotyping assays for bi-allelic markers (e.g. SNPs) produce
	signal intensities for the two alleles. 'fitPoly' assigns genotypes 
	(allele dosages) to a collection of polyploid samples based on these
	signal intensities. 'fitPoly' replaces the older package 'fitTetra' that was
	limited (a.o.) to only tetraploid populations whereas 'fitPoly' accepts any
	ploidy level. Reference: Voorrips RE, Gort G, Vosman B (2011)
	<doi:10.1186/1471-2105-12-172>.
	"""
	
	cran = "fitPoly" 

	version("3.0.0", md5="c636b58cd19f129d3593ee61030a7f89")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
