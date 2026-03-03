# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeckmanem(RPackage):
	"""Fit Normal or Student-t Heckman Selection Models

	It performs maximum likelihood estimation for the Heckman selection model (Normal or Student-t) using an EM-algorithm <doi:10.1016/j.jmva.2021.104737>. It also performs influence diagnostic through global and local influence for four possible perturbation schema. 
	"""
	
	cran = "HeckmanEM" 

	version("0.2-0", md5="d8ee34009711980bb982b72c84eaacb8")

	depends_on("r-mvtnorm@1.1.0:", type=("build", "run"))
	depends_on("r-sampleselection@1.2.6:", type=("build", "run"))
	depends_on("r-momtrunc@5.79:", type=("build", "run"))
	depends_on("r-performanceanalytics@2.0.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
