# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCommonsmath(RPackage):
	"""JAR Files of the Apache Commons Mathematics Library

	'Java' JAR files for the Apache Commons Mathematics Library for use by users and other packages.
	"""
	
	homepage = "https://github.com/dbdahl/commonsMath"
	cran = "commonsMath" 

	version("1.2.8", md5="23ea1fbd317970cce285beabe0af3d6b")

