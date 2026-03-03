# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsconsole(RPackage):
	"""A 'RStudio' Addin to Send 'JavaScript' Code to the 'V8' Console

	Provides a 'RStudio' addin to send some 'JavaScript' code to the 'V8' console. The user can send an entire 'JavaScript' file or only some selected lines. This is useful to test the code.
	"""
	
	homepage = "https://github.com/stla/JSconsole"
	cran = "JSconsole" 

	version("0.1.0", md5="95142cf6d0a3f0a7f2ad8b4a3865c160")

	depends_on("r-v8", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
