# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakefiler(RPackage):
	"""Create 'Makefiles' Using R

	A user-friendly interface for the construction of
        'Makefiles'.
	"""
	
	homepage = "http://krlmlr.github.io/MakefileR"
	cran = "MakefileR" 

	version("1.0", md5="fd7ec01a00d5fcdedeb19844d5e76cd4")

	depends_on("r-magrittr", type=("build", "run"))
