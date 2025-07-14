# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimalflowdata(RPackage):
	"""optimalFlowData

	Data files used as examples and for testing of the software provided in the optimalFlow package.
	"""
	
	bioc = "optimalFlowData"

	version("1.20.0", commit="ba14c0977491be3bdff7a0c7cb7eaad2e85e801e")
	version("1.14.0", commit="11b8946134d1717a947e12550365e26dd979f3f5")

	depends_on("r@4:", type=("build", "run"))

