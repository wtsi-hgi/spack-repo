# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopkin(RPackage):
	"""Estimate Kinship and FST under Arbitrary Population Structure

	Provides functions to estimate the kinship matrix of individuals from a large set of biallelic SNPs, and extract inbreeding coefficients and the generalized FST (Wright's fixation index).  Method described in Ochoa and Storey (2021) <doi:10.1371/journal.pgen.1009241>.
	"""
	
	homepage = "https://github.com/StoreyLab/popkin/"
	cran = "popkin" 

	version("1.3.23", md5="e69aba028e4ae50bded681c2baf47eae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
