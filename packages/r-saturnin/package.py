# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSaturnin(RPackage):
	"""Spanning Trees Used for Network Inference

	Bayesian inference of graphical model structures using spanning trees.
	"""
	
	cran = "saturnin" 

	version("1.1.1", md5="88adf97431cd17234c01a3fd42cf788c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
