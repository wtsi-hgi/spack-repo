# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgseg3d(RPackage):
	"""Tri-Surface Mesh Plots for Brain Atlases

	Mainly contains a plotting function ggseg3d(), 
    and data of two standard brain atlases (Desikan-Killiany and aseg). 
    By far, the largest bit of the package is the data for each of the atlases.
    The functions and data enable users to plot tri-surface mesh plots of
    brain atlases, and customise these by projecting colours onto the brain
    segments based on values in their own data sets. Functions are wrappers
    for 'plotly'. Mowinckel & Vidal-Piñeiro (2020)
    <doi:10.1177/2515245920928009>.
	"""
	
	homepage = "https://github.com/ggseg/ggseg3d/"
	cran = "ggseg3d" 

	version("1.6.3", md5="0316f14cf201dfa0ccbb32e1ff1ebf1a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
