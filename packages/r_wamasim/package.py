# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWamasim(RPackage):
	"""Simulate Rehabilitation Strategies for Water Distribution
Systems

	The outcome of various rehabilitation strategies for water distribution systems can be modeled with the Water Management Simulator (WaMaSim). Pipe breaks and the corresponding damage and rehabilitation costs are simulated. It is mainly intended to be used as educational tool for the Water Infrastructure Experimental and Computer Laboratory at ETH Zurich, Switzerland.
	"""
	
	homepage = "https://github.com/scheidan/WaMaSim"
	cran = "WaMaSim" 

	version("1.0.0", md5="6dbd6a5d742a7fb7696afec67fddd237")

	depends_on("r-magrittr@1.5:", type=("build", "run"))
