# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZscorer(RPackage):
	"""Child Anthropometry z-Score Calculator

	A tool for calculating z-scores and centiles for weight-for-age, 
    length/height-for-age, weight-for-length/height, BMI-for-age, 
    head circumference-for-age, age circumference-for-age, 
    subscapular skinfold-for-age, triceps skinfold-for-age based on the 
    WHO Child Growth Standards. 
	"""
	
	homepage = "https://github.com/nutriverse/zscorer"
	cran = "zscorer" 

	version("0.3.1", md5="3b387940a0bbd6c36a2da7cd5f206d62")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
