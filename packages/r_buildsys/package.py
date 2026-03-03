# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBuildsys(RPackage):
	"""System for Building and Debugging C/C++ Dynamic Libraries

	A build system based on 'GNU make' that creates and
    maintains (simply) make files in an R session and provides
    GUI debugging support through 'Microsoft Visual Code'.
	"""
	
	homepage = "https://github.com/pjumppanen/BuildSys"
	cran = "BuildSys" 

	version("1.1.2", md5="5d36d0968b4a4792161f9cf900c63dc5")

	depends_on("r-digest", type=("build", "run"))
