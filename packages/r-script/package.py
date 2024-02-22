# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScript(RPackage):
	"""Identify Script Name

	Identifies the name of the current script
    in a variety of contexts, e.g. interactively or 
    when sourced.  Attempts to support RStudio environment.
    Based on <https://stackoverflow.com/a/32016824/2292993>
    and <https://stackoverflow.com/a/35842176/2292993>.
	"""
	
	cran = "script" 

	version("0.1.1", md5="a0242e3fd4c0992f581d907570821c40")

	depends_on("r-rstudioapi", type=("build", "run"))
