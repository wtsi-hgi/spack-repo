# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpaex(RPackage):
	"""Automatic Detection of Experimental Unit in Precision
Agriculture

	A part of precision agriculture is linked to the spectral image obtained from the cameras. With the image information of the agricultural experiment, the included functions facilitate the collection of spectral data associated with the experimental units. Some designs generated in R are linked to the images, which allows the use of the information of each pixel of the image in the experimental unit and the treatment. Tables and images are generated for the analysis of the precision agriculture experiment during the entire vegetative period of the crop.
	"""
	
	cran = "rPAex" 

	version("1.0.5", md5="13064a3933a7a377140b7366342c991b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
