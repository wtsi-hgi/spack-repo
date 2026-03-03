# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliff(RPackage):
	"""Execute Command Line Programs Interactively

	Execute command line programs and format results for interactive use. It is based on the package 'processx' so it does not use shell to start up the process like system() and system2(). It also provides a simpler and cleaner interface than processx::run().
	"""
	
	homepage = "https://github.com/RTagBot/cliff"
	cran = "cliff" 

	version("0.1.2", md5="ce1f1d50ce47e05e190be3d856d2fbfb")

	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
