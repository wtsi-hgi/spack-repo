# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolysat(RPackage):
	"""Tools for Polyploid Microsatellite Analysis

	A collection of tools to handle microsatellite data of
 any ploidy (and samples of mixed ploidy) where allele copy number is not
 known in partially heterozygous genotypes.  It can import and export data in
 ABI 'GeneMapper', 'Structure', 'ATetra', 'Tetrasat'/'Tetra', 'GenoDive', 'SPAGeDi',
 'POPDIST', 'STRand', and binary presence/absence formats.  It can calculate
 pairwise distances between individuals using a stepwise mutation model or
 infinite alleles model, with or without taking ploidies and allele frequencies
 into account.  These distances can be used for the calculation of clonal
 diversity statistics or used for further analysis in R.  Allelic diversity
 statistics and Polymorphic Information Content are also available.  polysat can 
 assist the user in estimating the ploidy of samples, and it can estimate allele 
 frequencies in populations, calculate pairwise or global differentiation statistics 
 based on those frequencies, and export allele frequencies to 'SPAGeDi' and 'adegenet'.  
 Functions are also included for assigning alleles to isoloci in cases where one pair 
 of microsatellite primers amplifies alleles from two or more independently
 segregating isoloci.  polysat is described by Clark and Jasieniuk (2011)
 <doi:10.1111/j.1755-0998.2011.02985.x> and Clark and Schreier (2017)
 <doi:10.1111/1755-0998.12639>.
	"""
	
	homepage = "https://github.com/lvclark/polysat/wiki"
	cran = "polysat" 

	version("1.7-7", md5="1dc940d49e1f62523c29b70350db769f")

	depends_on("r-rcpp", type=("build", "run"))
