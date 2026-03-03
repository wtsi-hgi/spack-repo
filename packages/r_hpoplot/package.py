# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpoplot(RPackage):
	"""Functions for Plotting HPO Terms

	Collection of functions for manipulating sets of HPO terms and
    plotting them with a various options.
	"""
	
	cran = "hpoPlot" 

	version("2.4", md5="5d390d5c3a33ee7e749903fc5ea1ff38")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
