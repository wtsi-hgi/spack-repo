# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTetrascatt(RPackage):
	"""Acoustic Scattering for Complex Shapes by Using the DWBA

	Uses the Distorted Wave Born Approximation (DWBA) to compute the
  acoustic backward scattering, the geometry of the object is formed by a
  volumetric mesh, composed of tetrahedrons. This computation is done efficiently
  through an analytical 3D integration that allows for a solution which is
  expressed in terms of elementary functions for each tetrahedron.
  It is important to note that this method is only valid for objects whose
  acoustic properties, such as density and sound speed, do not vary significantly
  compared to the surrounding medium. (See Lavia, Cascallares and Gonzalez, J. D. (2023). 
  TetraScatt model: Born approximation for the estimation of acoustic dispersion of 
  fluid-like objects of arbitrary geometries. arXiv preprint <arXiv:2312.16721>).
	"""
	
	cran = "tetrascatt" 

	version("0.1.1", md5="f203f6163f9b3c050b7406198d33cdf1")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
