# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimrestore(RPackage):
	"""Simulate the Effect of Management Policies on Restoration
Efforts

	Simulation methods to study the effect of management policies on
    efforts to restore populations back to their original genetic composition.
    Allows for single-scenario simulation and for optimization of specific chosen
    scenarios. Further information can be found in Hernandez, Janzen and Lavretsky 
    (2023) <doi:10.1111/1755-0998.13892>. 
	"""
	
	cran = "simRestore" 

	version("1.1.4", md5="91361d06ac894616c16678922b9dca01")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-subplex", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
