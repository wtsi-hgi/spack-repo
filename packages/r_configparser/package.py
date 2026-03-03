# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfigparser(RPackage):
	"""Package to Parse an INI File, Including Variable Interpolation

	Enhances the 'ini' package by adding the ability to interpolate variables.
	     The INI configuration file is read into an R6 ConfigParser object (loosely inspired by Pythons ConfigParser module)
	     and the keys can be read, where '%(....)s' instances are interpolated by other included options or outside variables.
	"""
	
	homepage = "https://github.com/hhoeflin/ConfigParser"
	cran = "ConfigParser" 

	version("1.0.0", md5="06e2ea14f4178b13f668afe720aee7a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ini", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
