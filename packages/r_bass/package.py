# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBass(RPackage):
	"""Bayesian Adaptive Spline Surfaces

	Bayesian fitting and sensitivity analysis methods for adaptive
    spline surfaces described in <doi:10.18637/jss.v094.i08>. Built to handle continuous and categorical inputs as well as
    functional or scalar output. An extension of the methodology in Denison, Mallick
    and Smith (1998) <doi:10.1023/A:1008824606259>.
	"""
	
	cran = "BASS" 

	version("1.3.1", md5="2ca28d09e3d53a6a479771c6754e4471")

	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-hypergeo", type=("build", "run"))
