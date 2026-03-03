# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonophy(RPackage):
	"""Explore Monophyly of Taxonomic Groups in a Phylogeny

	Requires rooted phylogeny as input and creates a table of genera, their monophyly-status, which taxa cause problems in monophyly etc. Different information can be extracted from the output and a plot function allows visualization of the results in a number of ways. 
 "MonoPhy: a simple R package to find and visualize monophyly issues." Schwery, O. & O'Meara, B.C. (2016) <doi:10.7717/peerj-cs.56>.
	"""
	
	cran = "MonoPhy" 

	version("1.3", md5="b5a3671654cfbaf2e7057b9d23d9465f")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
