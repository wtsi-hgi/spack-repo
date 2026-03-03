# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixoptim(RPackage):
	"""Mixture Optimization Algorithm

	Simple tools to perform mixture optimization based on the 'desirability' package by Max Kuhn.
    It also provides a plot routine using 'ggplot2' and 'patchwork'.
	"""
	
	cran = "MixOptim" 

	version("0.1.2", md5="74c31632626cd094281926b494351b4a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-desirability", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
