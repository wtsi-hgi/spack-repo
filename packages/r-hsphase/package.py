# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsphase(RPackage):
	"""Phasing, Pedigree Reconstruction, Sire Imputation and
Recombination Events Identification of Half-sib Families Using
SNP Data

	Identification of recombination events, haplotype reconstruction, sire imputation and pedigree reconstruction using half-sib family SNP data.
	"""
	
	cran = "hsphase" 

	version("2.0.3", md5="156a0aff571e886689fc0bad8cd8a407")

	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp@0.11.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.300.8:", type=("build", "run"))
