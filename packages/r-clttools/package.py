# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClttools(RPackage):
	"""Central Limit Theorem Experiments (Theoretical and Simulation)

	Central limit theorem experiments presented by data frames or plots. Functions include generating theoretical sample space, corresponding probability, and simulated results as well.
	"""
	
	cran = "clttools" 

	version("1.3", md5="3340954f322ed8b298dfc2ca3492bb47")

