# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFractalparameterestimation(RPackage):
	"""Simulation and Parameter Estimation of Randomized Sierpinski
Carpets using the p-p-p-q-Model

	The parameters p and q are estimated with the aid of a randomized Sierpinski Carpet which is built on a [p-p-p-q]-model. Thereby, for three times a simulation with a p-value and once with a q-value is assumed. Hence, these parameters are estimated and displayed. Moreover, functions for simulating random Sierpinski-Carpets with constant and variable probabilities are included. For more details on the method please see Hermann et al. (2015) <doi:10.1002/sim.6497>. 
	"""
	
	cran = "FractalParameterEstimation" 

	version("1.1.2", md5="179e52975fd7c73e037d733b61d8bcbc")

	depends_on("r@2.2:", type=("build", "run"))
