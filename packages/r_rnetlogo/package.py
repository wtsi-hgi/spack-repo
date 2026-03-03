# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnetlogo(RPackage):
	"""Provides an Interface to the Agent-Based Modelling Platform
'NetLogo'

	Interface to use and access Wilensky's 'NetLogo' (Wilensky 1999) from R using either headless (no GUI) or interactive GUI mode. Provides functions to load models, execute commands, and get values from reporters. Mostly analogous to the 'NetLogo' 'Mathematica' Link <https://github.com/NetLogo/Mathematica-Link>.
	"""
	
	homepage = "http://rnetlogo.r-forge.r-project.org/"
	cran = "RNetLogo" 

	version("1.0-4", md5="af90f1f7aa8cea197549f13cae0cb6dd")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-rjava@0.9.8:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
