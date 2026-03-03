# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTripsanddipr(RPackage):
	"""Identification of 2n and 3n Samples from Amplicon Sequencing
Data

	Uses read counts for biallelic single nucleotide polymorphisms (SNPs)
    to compare the likelihoods for the observed read counts given that a sample is 
    either diploid or triploid. It allows parameters to be specified to account for 
    sequencing error rates and allelic bias. For details of the algorithm, please see
    Delomas (2019) <doi:10.1111/1755-0998.13073>.
	"""
	
	homepage = "https://github.com/delomast/tripsAndDipR"
	cran = "tripsAndDipR" 

	version("0.1.0", md5="15c96319524597a54e4dd836fd9a0341")

