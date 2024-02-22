# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixindependr(RPackage):
	"""Genetics and Independence Testing of Mixed Genetic Panels

	Developed to deal with multi-locus genotype data, this package is especially designed for those panel which include different type of markers. Basic genetic parameters like allele frequency, genotype frequency, heterozygosity and Hardy-Weinberg test of mixed genetic data can be obtained.     In addition, a new test for mutual independence which is compatible for mixed genetic data is developed in this package.
	"""
	
	homepage = "https://github.com/ice4prince/mixIndependR"
	cran = "mixIndependR" 

	version("1.0.0", md5="28115fb33b058bd39a62a5d7dd4eab93")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
