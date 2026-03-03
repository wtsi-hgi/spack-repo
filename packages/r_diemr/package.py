# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiemr(RPackage):
	"""Diagnostic Index Expectation Maximisation in R

	Likelihood-based genome polarisation finds which alleles of genomic markers 
    belong to which side of the barrier. 
	Co-estimates which individuals belong to either side of the barrier and barrier strength.
	Uses expectation maximisation in likelihood framework. The method is described in 
	Baird et al. (2023) <doi:10.1111/2041-210X.14010>.
	"""
	
	cran = "diemr" 

	version("1.2.2", md5="3da487ae126beea2a823fe98ba3f2709")

	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
