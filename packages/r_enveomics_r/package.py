# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnveomicsR(RPackage):
	"""Various Utilities for Microbial Genomics and Metagenomics

	A collection of functions for microbial ecology and other
   applications of genomics and metagenomics. Companion package for the
   Enveomics Collection (Rodriguez-R, L.M. and Konstantinidis, K.T., 2016
   <DOI:10.7287/peerj.preprints.1900v1>).
	"""
	
	homepage = "http://enve-omics.ce.gatech.edu/enveomics/"
	cran = "enveomics.R" 

	version("1.9.1", md5="35db702411f1fdc6fb8565cba106d38f")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-investr", type=("build", "run"))
