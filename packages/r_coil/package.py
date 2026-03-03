# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoil(RPackage):
	"""Contextualization and Evaluation of COI-5P Barcode Data

	Designed for the cleaning, contextualization and assessment of cytochrome c 
    oxidase I DNA barcode data (COI-5P, or the five prime portion of COI). It contains 
    functions for placing COI-5P barcode sequences into a common reading frame, 
    translating DNA sequences to amino acids and for assessing the likelihood that a 
    given barcode sequence includes an insertion or deletion error. The error assessment 
    relies on the comparison of input sequences against nucleotide and amino acid profile
    hidden Markov models (PHMMs) (for details see Durbin et al. 1998, ISBN: 9780521629713) 
    trained on a taxonomically diverse set of reference sequences. The functions are 
    provided as a complete pipeline and are also available individually for efficient and
    targeted analysis of barcode data.
	"""
	
	cran = "coil" 

	version("1.2.4", md5="41f21aaa133a70f2ea8f38d5808efe17")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-aphid", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
