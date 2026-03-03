# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHapi(RPackage):
	"""Inference of Chromosome-Length Haplotypes Using Genomic Data of
Single Gamete Cells

	Inference of chromosome-length haplotypes using a few haploid 
	gametes of an individual. The gamete genotype data may be generated from various platforms 
	including genotyping arrays and sequencing even with low-coverage. Hapi simply takes 
	genotype data of known hetSNPs in single gamete cells as input and report the high-resolution 
	haplotypes as well as confidence of each phased hetSNPs. The package also includes a module 
	allowing downstream analyses and visualization of identified crossovers in the gametes. 
	"""
	
	cran = "Hapi" 

	version("0.0.3", md5="297b757827304e505c145f1615755534")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-hmm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
