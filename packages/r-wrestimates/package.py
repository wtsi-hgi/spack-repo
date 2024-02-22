# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrestimates(RPackage):
	"""Sample Size, Power and CI for the Win Ratio

	Calculates non-parametric estimates of the sample size, power and confidence intervals for the win-ratio. For more detail on the theory behind the methodologies implemented see Yu, R. X. and Ganju, J. (2022) <doi:10.1002/sim.9297>. 
	"""
	
	cran = "WRestimates" 

	version("0.1.0", md5="de99e97780a3b5c3e441df9a18c2b732")

