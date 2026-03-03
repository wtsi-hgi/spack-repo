# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibrarysnapshot(RPackage):
	"""Library Snapshot for Packages and Dependencies in Use by Current
Session

	Generate a local library copy with relevant packages. 
    All packages currently found within the search path - except base packages - 
    will be copied to the directory provided and can be used later on with the 
    .libPaths() function. 
	"""
	
	homepage = "https://github.com/petermeissner/librarysnapshot"
	cran = "librarysnapshot" 

	version("0.1.2", md5="d2b793e1aa360fc386a87047e54bf0d6")

