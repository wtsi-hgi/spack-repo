# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplot2movies(RPackage):
	"""Movies Data

	A dataset about movies. This was previously contained in ggplot2,
   but has been moved its own package to reduce the download size of ggplot2.
	"""
	
	cran = "ggplot2movies" 

	version("0.0.1", md5="cdb07bdf83c680ac2c2c4c6d867a08d3")

	depends_on("r@2.10:", type=("build", "run"))
