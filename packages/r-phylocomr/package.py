# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylocomr(RPackage):
	"""Interface to 'Phylocom'

	Interface to 'Phylocom' (<https://phylodiversity.net/phylocom/>),
    a library for analysis of 'phylogenetic' community structure and
    character evolution. Includes low level methods for interacting with
    the three executables, as well as higher level interfaces for methods
    like 'aot', 'ecovolve', 'bladj', 'phylomatic', and more.
	"""
	
	homepage = "https://docs.ropensci.org/phylocomr/"
	cran = "phylocomr" 

	version("0.3.4", md5="94c06556c684c9efb8c337205614c13e")

	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sys@3.2:", type=("build", "run"))
