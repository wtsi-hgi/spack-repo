# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXring(RPackage):
	"""Identify and Measure Tree Rings on X-Ray Micro-Density Profiles

	Contains functions to identify tree-ring borders based on X-ray micro-density profiles and a Graphical User Interface (GUI) to visualize density profiles and correct tree-ring borders. Campelo F, Mayer K, Grabner M. (2019) <doi:10.1016/j.dendro.2018.11.002>.
	"""
	
	cran = "xRing" 

	version("0.1.1", md5="b0d38e06370545b7abbe26e2478ab810")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-tkrplotr", type=("build", "run"))
