# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeeds(RPackage):
	"""Attaches and Installs Packages

	A simple function for easier package loading and auto-installation.
	"""
	
	homepage = "https://github.com/joshkatz/needs"
	cran = "needs" 

	version("0.0.3", md5="ebef6956f1bb0cf7c1911826a9a6f36f")

	depends_on("r@3.2:", type=("build", "run"))
