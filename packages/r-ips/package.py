# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIps(RPackage):
	"""Interfaces to Phylogenetic Software in R

	Functions that wrap popular phylogenetic software for sequence
    alignment, masking of sequence alignments, and estimation of phylogenies and
    ancestral character states.
	"""
	
	cran = "ips" 

	version("0.0.11", md5="04a4d849554757928522b01a1e8d2a47")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
