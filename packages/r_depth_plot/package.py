# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepthPlot(RPackage):
	"""Multivariate Analogy of Quantiles

	Could be used to obtain spatial depths, spatial ranks and outliers of multivariate random variables. Could also be used to visualize DD-plots (a multivariate generalization of QQ-plots).
	"""
	
	cran = "depth.plot" 

	version("0.1", md5="5271e739819c5770f5a8a226616f4aab")

	depends_on("r-mvtnorm", type=("build", "run"))
