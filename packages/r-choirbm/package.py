# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChoirbm(RPackage):
	"""Plots the CHOIR Body Map

	Collection of utility functions for visualizing
    body map data collected with the Collaborative Health Outcomes
    Information Registry.
	"""
	
	homepage = "https://github.com/emcramer/CHOIRBM"
	cran = "CHOIRBM" 

	version("0.0.2", md5="029b7e58f2a0c1ad4dadc2fe68406dac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
