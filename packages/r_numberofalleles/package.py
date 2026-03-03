# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumberofalleles(RPackage):
	"""Compute the Probability Distribution of the Number of Alleles in
a DNA Mixture

	The number of distinct alleles observed in a DNA mixture is informative of the number of contributors to the mixture. The package provides methods for computing the probability distribution of the number of distinct alleles in a mixture for a given set of allele frequencies. The mixture contributors may be related according to a provided pedigree.
	"""
	
	cran = "numberofalleles" 

	version("1.0.1", md5="2ba4f6930061a300ba951f5835b9acc1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pedtools", type=("build", "run"))
	depends_on("r-ribd", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
