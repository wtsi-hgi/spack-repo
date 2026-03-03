# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoms(RPackage):
	"""Phylogenetic Organization of Metagenomic Signals

	Code to identify functional enrichments across diverse taxa
    in phylogenetic tree, particularly where these taxa differ in
    abundance across samples in a non-random pattern. The motivation for
    this approach is to identify microbial functions encoded by diverse
    taxa that are at higher abundance in certain samples compared to
    others, which could indicate that such functions are broadly adaptive
    under certain conditions. See 'GitHub' repository for tutorial and
    examples: <https://github.com/gavinmdouglas/POMS/wiki>. Citation: Gavin M. Douglas, Molly G. Hayes, Morgan G. I. Langille, Elhanan Borenstein (2022) <doi:10.1093/bioinformatics/btac655>.
	"""
	
	cran = "POMS" 

	version("1.0.1", md5="1f1531616746e4b502b51802d43a53e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-phangorn@2:", type=("build", "run"))
	depends_on("r-phylolm@2.6:", type=("build", "run"))
	depends_on("r-xnomial@1.0.4:", type=("build", "run"))
