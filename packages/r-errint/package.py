# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErrint(RPackage):
	"""Builds Error Intervals

	Builds and analyzes error intervals for a particular model predictions assuming different distributions for noise in the data.
	"""
	
	homepage = "http://link.springer.com/chapter/10.1007/978-3-319-19222-2_47"
	cran = "errint" 

	version("1.0", md5="060a969ed9a050e6c53fde06a53445fd")

	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
