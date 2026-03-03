# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGettz(RPackage):
	"""Get the Timezone Information

	A function to retrieve the system timezone on Unix systems
 which has been found to find an answer when 'Sys.timezone()' has failed.
 It is based on an answer by Duane McCully posted on 'StackOverflow', and
 adapted to be callable from R. The package also builds on Windows, but
 just returns NULL.
	"""
	
	homepage = "https://github.com/eddelbuettel/gettz/"
	cran = "gettz" 

	version("0.0.5", md5="97ec8287ff233fda2ae794f30d681ad3")

