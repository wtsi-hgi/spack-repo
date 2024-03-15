# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimDiffproc(RPackage):
	"""Simulation of Diffusion Processes

	It provides users with a wide range of tools to simulate, estimate, analyze, and visualize the dynamics of stochastic differential systems in both forms Ito and Stratonovich. Statistical analysis with parallel Monte Carlo and moment equations methods of SDEs <doi:10.18637/jss.v096.i02>. Enabled many searchers in different domains to use these equations to modeling practical problems in financial and actuarial modeling and other areas of application, e.g., modeling and simulate of first passage time problem in shallow water using the attractive center (Boukhetala K, 1996) ISBN:1-56252-342-2. 
	"""
	
	homepage = "https://github.com/acguidoum/Sim.DiffProc"
	cran = "Sim.DiffProc" 

	version("4.9", md5="0732efe881297332ac69ed83ca6dc151")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-deriv@3.8:", type=("build", "run"))
	depends_on("r-mass@7.3.30:", type=("build", "run"))
