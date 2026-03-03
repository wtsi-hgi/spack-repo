# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakeflow(RPackage):
	"""Visualizing Sequential Classifications

	A user-friendly tool for visualizing categorical or group movement.
	"""
	
	cran = "makeFlow" 

	version("1.0.2", md5="7a31b51a5303d7aa22543b04180faf83")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
