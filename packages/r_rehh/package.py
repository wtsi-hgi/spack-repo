# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRehh(RPackage):
	"""Searching for Footprints of Selection using 'Extended Haplotype
Homozygosity' Based Tests

	Population genetic data such as 'Single Nucleotide
        Polymorphisms' (SNPs) is often used to identify genomic regions
        that have been under recent natural or artificial selection
        and might provide clues about the molecular mechanisms of adaptation. 
        One approach, the concept of an 'Extended Haplotype Homozygosity' (EHH), 
        introduced by (Sabeti 2002) <doi:10.1038/nature01140>, has given rise to 
        several statistics designed for whole genome scans. 
        The package provides functions to compute three of these,
        namely: 'iHS' (Voight 2006) <doi:10.1371/journal.pbio.0040072> for
        detecting positive or 'Darwinian' selection within a single population as well as
        'Rsb' (Tang 2007) <doi:10.1371/journal.pbio.0050171> and 
        'XP-EHH' (Sabeti 2007) <doi:10.1038/nature06250>, targeted
        at differential selection between two populations. 
        Various plotting functions are included to facilitate
        visualization and interpretation of these statistics.
	"""
	
	homepage = "https://CRAN.R-project.org/package=rehh"
	cran = "rehh" 

	version("3.2.2", md5="ba325e4c182d3288f3eaabb1a736237d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rehh-data", type=("build", "run"))
