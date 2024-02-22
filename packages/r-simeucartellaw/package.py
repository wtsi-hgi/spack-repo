# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimeucartellaw(RPackage):
	"""Simulation of Legal Exemption System for European Cartel Law

	Monte Carlo simulations of a game-theoretic model for the 
	legal exemption system of the European cartel law are implemented
	in order to estimate the (mean) deterrent effect of this system.
	The input and output parameters of the simulated cartel 
	opportunities can be visualized by three-dimensional projections.
	A description of the model is given in Moritz et al. (2018)
	<doi:10.1515/bejeap-2017-0235>.
	"""
	
	cran = "SimEUCartelLaw" 

	version("1.0.3", md5="51747907845157d7db4352f4fdf77100")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
