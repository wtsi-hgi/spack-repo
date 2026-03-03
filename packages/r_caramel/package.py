# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaramel(RPackage):
	"""Automatic Calibration by Evolutionary Multi Objective Algorithm

	Multi-objective optimizer initially developed for the calibration of hydrological models.
     The algorithm is a hybrid of the MEAS algorithm (Efstratiadis and Koutsoyiannis (2005) <doi:10.13140/RG.2.2.32963.81446>) by using the directional search method based on the simplexes of the objective space
     and the epsilon-NGSA-II algorithm with the method of classification of the parameter vectors archiving management by epsilon-dominance (Reed and Devireddy <doi:10.1142/9789812567796_0004>).
	"""
	
	homepage = "https://github.com/fzao/caRamel"
	cran = "caRamel" 

	version("1.3", md5="62163eea006884c6791956dd484ac62e")

	depends_on("r-geometry", type=("build", "run"))
