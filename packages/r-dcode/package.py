# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcode(RPackage):
	"""List Linear n-Peptide Constraints for Overlapping Protein
Regions

	Traversal graph algorithm for listing linear n-peptide constraints for overlapping protein regions. (Lebre and Gascuel, The combinatorics of overlapping genes, freely available from arXiv at : http://arxiv.org/abs/1602.04971). 
	"""
	
	cran = "DCODE" 

	version("1.0", md5="ded5e9fc189a0443ec1620cefd641b17")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
