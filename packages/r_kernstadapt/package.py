# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernstadapt(RPackage):
	"""Spatio-Temporal Adaptive Kernel Estimators for Intensities

	Adaptive estimation of the first-order intensity function of a spatio-temporal point process using kernels and variable bandwidths. The methodology used for estimation is presented in González and Moraga (2022). <arXiv:2208.12026>.
	"""
	
	cran = "kernstadapt" 

	version("0.0.2", md5="76b14331feeb401fe48772512e5a488e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-misc3d", type=("build", "run"))
	depends_on("r-sparr", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
