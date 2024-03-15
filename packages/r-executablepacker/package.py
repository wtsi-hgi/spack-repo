# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExecutablepacker(RPackage):
	"""Make 'shiny' App to Executable Program

	Make your 'shiny' application as executable program. 
    Users do not need to install 'R' and 'shiny' on their system.
	"""
	
	cran = "executablePackeR" 

	version("0.0.2", md5="f66bdf2a6c200a0b1313289a1deeffd3")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-automagic", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
