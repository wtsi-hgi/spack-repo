# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLobstercatch(RPackage):
	"""Models the Capture Processes in American Lobster Trap Fishery

	Simulate lobster catch process in a trap fishery. Factors such as lobster density on ocean floor, their movement, trap saturation and bait shrinkage rate can be modeled. Details of the methods for modeling those processes can be found in: Addison and Bell (1997) <doi:10.1071/MF97169>.
	"""
	
	cran = "LobsterCatch" 

	version("0.1.0", md5="d0feab9801a834c7f8f11216ce989a21")

	depends_on("r@2.10:", type=("build", "run"))
