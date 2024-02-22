# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLspfp(RPackage):
	"""Lysate and Secretome Peptide Feature Plotter

	Creates plots of peptides from shotgun proteomics analysis of secretome and lysate samples. These plots contain associated protein features and scores for potential secretion and truncation.
	"""
	
	cran = "LSPFP" 

	version("1.0.3", md5="d537583be2e3b986188cae5abf20d9f4")

	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
