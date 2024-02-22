# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalinsol(RPackage):
	"""Insolation for Palaeoclimate Studies

	R package to compute Incoming Solar Radiation (insolation) for palaeoclimate studies. Features three solutions: Berger (1978), Berger and Loutre (1991) and Laskar et al. (2004). Computes daily-mean, season-averaged and annual means and for all latitudes, and polar night dates.
	"""
	
	homepage = "https://github.com/mcrucifix/palinsol"
	cran = "palinsol" 

	version("1.0", md5="01aba1d431d232b4c09643e7e00e59c8")

	depends_on("r@2.10:", type=("build", "run"))
