# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeastier(RPackage):
	"""Call 'BEAST2'

	'BEAST2' (<https://www.beast2.org>) is a widely used
    Bayesian phylogenetic tool, that uses DNA/RNA/protein data
    and many model priors to create a posterior of jointly estimated 
    phylogenies and parameters.
    'BEAST2' is a command-line tool.
    This package provides a way to call 'BEAST2' 
    from an 'R' function call.
	"""
	
	homepage = "https://docs.ropensci.org/beastier/"
	cran = "beastier" 

	version("2.5", md5="b9dfc62623575aacdd43d72cbf8c99a7")

	depends_on("r-ape", type=("build", "run"))
	depends_on("r-beautier@2.6.11:", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("beast2", type=("build", "link", "run"))
