# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprofile(RPackage):
	"""Load Both User-Global and Project-Specific R Profile
Configurations

	Use rprofile::load() inside a project '.Rprofile' file to ensure that the user-global '.Rprofile' is
  loaded correctly regardless of its location, and other common resources (in particular 'renv') are also set up
  correctly.
	"""
	
	cran = "rprofile" 

	version("0.4.0", md5="2bd7f5534bdb78d9b0b44e1c7aac3430")

	depends_on("r@4.1:", type=("build", "run"))
