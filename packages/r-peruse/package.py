# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeruse(RPackage):
	"""A Tidy API for Sequence Iteration and Set Comprehension

	A friendly API for sequence iteration and set comprehension.
	"""
	
	homepage = "https://github.com/jacgoldsm/peruse"
	cran = "peruse" 

	version("0.3.1", md5="a2d844a8ddf4db7129bce9e572f3d156")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
