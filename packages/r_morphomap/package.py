# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorphomap(RPackage):
	"""Morphometric Maps, Bone Landmarking and Cross Sectional Geometry

	Extract cross sections from long bone meshes at specified intervals along the diaphysis. Calculate two and three-dimensional morphometric maps, cross-sectional geometric parameters, and semilandmarks on the periosteal and endosteal contours of each cross section. 
	"""
	
	cran = "morphomap" 

	version("1.5", md5="3acaf12abfb5f6b89361f67bb82170ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arothron@1:", type=("build", "run"))
	depends_on("r-lattice@0.2:", type=("build", "run"))
	depends_on("r-mgcv@1.8:", type=("build", "run"))
	depends_on("r-rvcg@0.18:", type=("build", "run"))
	depends_on("r-morpho@2:", type=("build", "run"))
	depends_on("r-oce@1.1:", type=("build", "run"))
	depends_on("r-sp@1.3:", type=("build", "run"))
	depends_on("r-geometry@0.4:", type=("build", "run"))
	depends_on("r-rgl@0.1:", type=("build", "run"))
	depends_on("r-colorramps@2.3:", type=("build", "run"))
	depends_on("r-desctools@0.99:", type=("build", "run"))
