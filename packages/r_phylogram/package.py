# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylogram(RPackage):
	"""Dendrograms for Evolutionary Analysis

	Contains functions for developing phylogenetic trees as
    deeply-nested lists ("dendrogram" objects).
    Enables bi-directional conversion between dendrogram and
    "phylo" objects
    (see Paradis et al (2004) <doi:10.1093/bioinformatics/btg412>),
    and features several tools for command-line tree
    manipulation and import/export via Newick parenthetic text.
	"""
	
	homepage = "http://github.com/ropensci/phylogram"
	cran = "phylogram" 

	version("2.1.0", md5="9527ae1f02ca8bc5cd3e8caa9e57d61c")

	depends_on("r-ape@4:", type=("build", "run"))
