# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimsalapar(RPackage):
	"""Tools for Simulation Studies in Parallel

	Tools for setting up ("design"), conducting, and evaluating
  large-scale simulation studies with graphics and tables, including
  parallel computations.
	"""
	
	cran = "simsalapar" 

	version("1.0-12", md5="cd083a99f7be5315c9d02399dde2194a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-gridbase@0.4.6:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
