# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDang(RPackage):
	"""'Dang' Associated New Goodies

	A collection of utility functions.
	"""
	
	homepage = "https://github.com/eddelbuettel/dang"
	cran = "dang" 

	version("0.0.16", md5="ab932470011918ef4275669eeb7c65e5")

	depends_on("r-tidycpp", type=("build", "run"))
