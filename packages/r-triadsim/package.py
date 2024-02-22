# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriadsim(RPackage):
	"""Simulating Triad Genomewide Genotypes

	Simulate genotypes for case-parent triads, case-control, and quantitative trait samples with realistic linkage diequilibrium structure and allele frequency distribution. For studies of epistasis one can simulate models that involve specific SNPs at specific sets of loci, which we will refer to as "pathways". TriadSim generates genotype data by resampling triad genotypes from existing data. The details of the method is described in the manuscript under preparation "Simulating Autosomal Genotypes with Realistic Linkage Disequilibrium and a Spiked in Genetic Effect" Shi, M., Umbach, D.M., Wise A.S., Weinberg, C.R. 	
	"""
	
	cran = "TriadSim" 

	version("0.3.0", md5="c9a5e0f5b0220146cae01238c89f99b1")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-snpstats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
