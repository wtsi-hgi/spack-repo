# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaux(RPackage):
	"""Simulation for Factorial Designs

	Create datasets with factorial structure through simulation by specifying variable parameters. Extended documentation at <https://debruine.github.io/faux/>. Described in DeBruine (2020) <doi:10.5281/zenodo.2669586>.
	"""
	
	homepage = "https://github.com/debruine/faux"
	cran = "faux" 

	version("1.2.1", md5="3eafbcc685019a44dabe5cd3a1fd0c15")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
