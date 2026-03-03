# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsmrealoptions(RPackage):
	"""Value American and Real Options Through LSM Simulation

	The least-squares Monte Carlo (LSM) simulation method is a popular method for the approximation of the value of early and multiple exercise options. 'LSMRealOptions' provides implementations of the LSM simulation method to value American option products and capital investment projects through real options analysis. 'LSMRealOptions' values capital investment projects with cash flows dependent upon underlying state variables that are stochastically evolving, providing analysis into the timing and critical values at which investment is optimal. 'LSMRealOptions' provides flexibility in the stochastic processes followed by underlying assets, the number of state variables, basis functions and underlying asset characteristics to allow a broad range of assets to be valued through the LSM simulation method. Real options projects are further able to be valued whilst considering construction periods, time-varying initial capital expenditures and path-dependent operational flexibility including the ability to temporarily shutdown or permanently abandon projects after initial investment has occurred. The LSM simulation method was first presented in the prolific work of Longstaff and Schwartz (2001) <doi:10.1093/rfs/14.1.113>.
	"""
	
	cran = "LSMRealOptions" 

	version("0.2.1", md5="638387e8669f71465355204744c1a8ec")

	depends_on("r@3.5:", type=("build", "run"))
