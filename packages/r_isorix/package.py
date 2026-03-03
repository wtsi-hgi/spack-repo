# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsorix(RPackage):
	"""Isoscape Computation and Inference of Spatial Origins using
Mixed Models

	Building isoscapes using mixed models and inferring the geographic
  origin of samples based on their isotopic ratios. This package is essentially a
  simplified interface to several other packages which implements a new
  statistical framework based on mixed models. It uses 'spaMM' for fitting and
  predicting isoscapes, and assigning an organism's origin depending on its
  isotopic ratio. 'IsoriX' also relies heavily on the package 'rasterVis' for
  plotting the maps produced with 'terra' using 'lattice'.
	"""
	
	homepage = "https://github.com/courtiol/IsoriX"
	cran = "IsoriX" 

	version("0.9.2", md5="3bd3bf7b11f1bcce8e377fd7ce580bb1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice@0.22.2:", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rastervis@0.51.6:", type=("build", "run"))
	depends_on("r-spamm@3.13:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
