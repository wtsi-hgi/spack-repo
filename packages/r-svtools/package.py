# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvtools(RPackage):
	"""Wrappers for Tools in Other Packages for IDE Friendliness

	Set of tools aimed at wrapping some of the functionalities of the
  packages tools, utils and codetools into a nicer format so that an IDE can use
  them.
	"""
	
	homepage = "http://www.sciviews.org/SciViews-R"
	cran = "svTools" 

	version("0.9-5", md5="7c17755eb0d6f91bce24f76683c0bcdf")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
	depends_on("r-svmisc", type=("build", "run"))
