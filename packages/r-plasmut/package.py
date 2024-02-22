# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlasmut(RPackage):
	"""Stratifying mutations observed in cell-free DNA and white blood cells as germline, hematopoietic, or somatic

	A Bayesian method for quantifying the liklihood that a given plasma mutation arises from clonal hematopoesis or the underlying tumor. It requires sequencing data of the mutation in plasma and white blood cells with the number of distinct and mutant reads in both tissues. We implement a Monte Carlo importance sampling method to assess the likelihood that a mutation arises from the tumor relative to non-tumor origin.
	"""
	
	bioc = "plasmut" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/plasmut_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/plasmut/plasmut_1.0.0.tar.gz"]

	version("1.0.0", md5="8681d905157c0cbb8b46e48cbe4ecde9")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
