# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCurvedepth(RPackage):
	"""Tukey Curve Depth and Distance in the Space of Curves

	Data recorded as paths or trajectories may be suitably described 
  by curves, which are independent of their parametrization. For the space of 
  such curves, the package provides functionalities for reading curves, sampling 
  points on curves, calculating distance between curves and for computing Tukey
  curve depth of a curve w.r.t. to a bundle of curves. For details see 
  Lafaye De Micheaux, Mozharovskyi, and Vimond (2019) <arXiv:1901.00180>.
	"""
	
	cran = "curveDepth" 

	version("0.1.0.9", md5="6310a71dd37659347871163214192669")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ddalpha", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
