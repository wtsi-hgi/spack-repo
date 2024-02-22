# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptifunset(RPackage):
	"""Set Options if Unset

	A single function 'options.ifunset(...)' is contained herewith, which allows the user to set a global option ONLY if it is not already set. By this token, for package maintainers this function can be used in preference to the standard 'options(...)' function, making provision for THEIR end user to place 'options(...)' directives within their '.Rprofile' file, which will not be overridden at the point when a package is loaded.
	"""
	
	cran = "optifunset" 

	version("1.0", md5="95dfd58f584fc3fd08404c0e7e9bda3e")

