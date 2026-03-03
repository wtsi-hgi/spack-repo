# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRncbieutilslibs(RPackage):
	"""EUtils libraries for use in the R environment

	Provides the libraries of the EUtils operations for the
        RNCBI package.
	"""
	
	homepage = "https://code.google.com/p/rncbi/"
	cran = "RNCBIEUtilsLibs" 

	version("0.9", md5="6ffdb9f65f0c0b80340ae44bc84f76ed")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-rjava@0.8:", type=("build", "run"))
	depends_on("openjdk", type=("build", "link", "run"))
