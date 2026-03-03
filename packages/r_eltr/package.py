# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REltr(RPackage):
	"""Utilise Catastrophe Model Event Loss Table Outputs

	Provides a tool to run Monte Carlo simulation of catastrophe model event loss tables, using a Poisson frequency and Beta severity distribution.
	"""
	
	homepage = "https://randhirbilkhu.github.io/eltr/"
	cran = "eltr" 

	version("0.1.0", md5="3d0c43f69a39885901145ac24eca30ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
