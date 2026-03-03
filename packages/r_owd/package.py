# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROwd(RPackage):
	"""Open Working Directory

	Open the current working directory (or a given directory path) in your computer's file manager.
	"""
	
	homepage = "https://github.com/Feakster/owd"
	cran = "owd" 

	version("1.0.6", md5="7b4c0aabc48b63cf1860b2dcd1d067b1")

	depends_on("r@2.13:", type=("build", "run"))
