# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmEgo(RPackage):
	"""Fit, Simulate and Diagnose Exponential-Family Random Graph
Models to Egocentrically Sampled Network Data

	Utilities for managing egocentrically sampled network data and a wrapper around the 'ergm' package to facilitate ERGM inference and simulation from such data. See Krivitsky and Morris (2017) <doi:10.1214/16-AOAS1010>.
	"""
	
	homepage = "https://statnet.org"
	cran = "ergm.ego" 

	version("1.1.0", md5="b309bcdadc9d306ace298bbb1ac63a3b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ergm", type=("build", "run"))
	depends_on("r-egor", type=("build", "run"))
	depends_on("r-network@1.17.1:", type=("build", "run"))
	depends_on("r-statnet-common@4.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
