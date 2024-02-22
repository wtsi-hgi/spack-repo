# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimtool(RPackage):
	"""Conduct Simulation Studies with a Minimal Amount of Source Code

	Tool for statistical simulations that have two components. 
    One component generates the data and the other one
    analyzes the data. The main aims of the package are the reduction
    of the administrative source code (mainly loops and management code for the
    results) and a simple applicability of the package that allows the user to
    quickly learn how to work with it. Parallel computing is
    also supported. Finally, convenient functions are provided to summarize the
    simulation results.
	"""
	
	homepage = "https://github.com/MarselScheer/simTool"
	cran = "simTool" 

	version("1.1.7", md5="346c8bb94a8eeb854f8114b7971873f4")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
