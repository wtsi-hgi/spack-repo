# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisualizesimon2stage(RPackage):
	"""Visualize Simon's Two-Stage Design

	To visualize the probabilities of early
       termination, fail and success of Simon's two-stage
       design.  To evaluate and visualize the operating
       characteristics of Simon's two-stage design.
	"""
	
	cran = "VisualizeSimon2Stage" 

	version("0.1.3", md5="3410783d2ab598a3595ae3521c6a52f6")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
