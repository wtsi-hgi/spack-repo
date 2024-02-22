# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDartrverse(RPackage):
	"""Install and Load the 'dartRverse' Suits of Packages

	Provides a single function that supports the installation of all packages 
    belonging to the 'dartRverse'. The 'dartRverse' is a set of packages that work 
    together to analyse SNP (single nuclear polymorphism) data. All packages aim to have a similar 'look and feel' 
    and are based on the same type of data structure ('genlight'), with additional
    metadata for loci and individuals (samples). For more information visit the
    'GitHub' pages <https://github.com/green-striped-gecko/dartRverse>.
	"""
	
	homepage = "https://github.com/green-striped-gecko/dartRverse"
	cran = "dartRverse" 

	version("0.51", md5="d24c67fcdd110f66449b1b83d0d6cf93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dartr-base", type=("build", "run"))
	depends_on("r-dartr-data", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
