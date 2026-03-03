# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreebase(RPackage):
	"""Discovery, Access and Manipulation of 'TreeBASE' Phylogenies

	Interface to the API for 'TreeBASE' <http://treebase.org>
    from 'R.' 'TreeBASE' is a repository of user-submitted phylogenetic
    trees (of species, population, or genes) and the data used to create
    them.
	"""
	
	homepage = "https://docs.ropensci.org/treebase/"
	cran = "treebase" 

	version("0.1.5", md5="37b80de6c75fe8a991b7c4635fe12616")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
