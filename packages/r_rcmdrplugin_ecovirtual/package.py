# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginEcovirtual(RPackage):
	"""Rcmdr EcoVirtual Plugin

	A Rcmdr "plug-in" for the EcoVirtual package, designed primarily for teaching ecological models using simulations.
	"""
	
	homepage = "http://ecovirtual.ib.usp.br"
	cran = "RcmdrPlugin.EcoVirtual" 

	version("1.0", md5="c1b4aeb755fe891f88fcaf8263d6e4e3")

	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-ecovirtual", type=("build", "run"))
