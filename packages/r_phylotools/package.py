# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylotools(RPackage):
	"""Phylogenetic Tools for Eco-Phylogenetics

	A collection of tools for building RAxML supermatrix using
             PHYLIP or aligned FASTA files. These functions will be
             useful for building large phylogenies using multiple markers.
	"""
	
	homepage = "https://github.com/helixcn/phylotools"
	cran = "phylotools" 

	version("0.2.2", md5="e7258952e68082ffcf70cc20d49ec053")

	depends_on("r-ape", type=("build", "run"))
