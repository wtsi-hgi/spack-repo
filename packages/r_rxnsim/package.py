# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxnsim(RPackage):
	"""Functions to Compute Chemical and Chemical Reaction Similarity

	Methods to compute chemical similarity between two or more reactions and molecules. Allows masking of chemical substructures for weighted similarity computations. Uses packages 'rCDK' and 'fingerprint' for cheminformatics functionality. Methods for reaction similarity and sub-structure masking are as described in: Giri et al. (2015) <doi:10.1093/bioinformatics/btv416>. 
	"""
	
	cran = "RxnSim" 

	version("1.0.4", md5="79fa6851b7f45f4d51276a5caf8eb740")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-fingerprint", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcdk@3.8.1:", type=("build", "run"))
