# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetawho(RPackage):
	"""Meta-Analytical Implementation to Identify Who Benefits Most
from Treatments

	A tool for implementing so called 'deft' approach
    (see Fisher, David J., et al. (2017) <DOI:10.1136/bmj.j573>) and model
    visualization.
	"""
	
	homepage = "https://github.com/ShixiangWang/metawho"
	cran = "metawho" 

	version("0.2.0", md5="c7565cb7fd39c268302b7cd08dbf1350")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forestmodel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
