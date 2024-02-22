# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisperse(RPackage):
	"""Simulation of Demic Diffusion with Environmental Constraints

	Simulates demic diffusion building on models previously developed
	for the expansion of Neolithic and other food-producing economies during
	the Holocene (Fort et al. (2012) <doi:10.7183/0002-7316.77.2.203>, Souza et al.
	(2021) <doi:10.1098/rsif.2021.0499>). Growth and emigration are modelled as
	density-dependent processes using logistic growth and an asymptotic threshold
	model. Environmental and terrain layers, which can change over time, affect
	carrying capacity, growth and mobility. Multiple centres of origin with
	their respective starting times can be specified.
	"""
	
	cran = "dispeRse" 

	version("1.1", md5="69595eb5f6894892a8b27a3655db17b0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
