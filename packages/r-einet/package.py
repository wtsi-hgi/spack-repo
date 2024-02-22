# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REinet(RPackage):
	"""Effective Information and Causal Emergence

	Methods and utilities for causal emergence.
    Used to explore and compute various information theory metrics for networks, such as effective information, effectiveness and causal emergence.
	"""
	
	homepage = "https://github.com/travisbyrum/einet"
	cran = "einet" 

	version("0.1.0", md5="94f61167b7502f9a7fe7c3c179b377b0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
