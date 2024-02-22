# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDym(RPackage):
	"""Did You Mean?

	Add a "Did You Mean" feature to the R interactive. With this
    package, error messages for misspelled input of variable names or package names
    suggest what you really want to do in addition to notification of the mistake.
	"""
	
	cran = "DYM" 

	version("0.2", md5="ff50ae8da415bd963d91945456bab687")

