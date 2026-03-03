# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolypatex(RPackage):
	"""Paternity Exclusion in Autopolyploid Species

	Functions to perform paternity exclusion via allele
    matching, in autopolyploid species having ploidy 4, 6, or 8. The
    marker data used can be genotype data (copy numbers known) or
    'allelic phenotype data' (copy numbers not known).
	"""
	
	cran = "PolyPatEx" 

	version("0.9.2", md5="a2bcb3ceb22fff60739667383a1ce4dc")

	depends_on("r-gtools", type=("build", "run"))
