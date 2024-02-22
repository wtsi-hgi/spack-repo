# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKarel(RPackage):
	"""Learning programming with Karel the robot

	This is the R implementation of Karel the robot, a programming 
  language created by Dr. R. E. Pattis at Stanford University in 1981. Karel is 
  an useful tool to teach introductory concepts about general programming, such 
  as algorithmic decomposition, conditional statements, loops, etc., in an 
  interactive and fun way, by writing programs to make Karel the robot achieve 
  certain tasks in the world she lives in. Originally based on Pascal, Karel 
  was implemented in many languages through these decades, including 'Java', 'C++', 
  'Ruby' and 'Python'. This is the first package implementing Karel in R.
	"""
	
	homepage = "https://mpru.github.io/karel/"
	cran = "karel" 

	version("0.1.1", md5="05f74d70e098bd8833c89a84d0c501ef")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-gifski", type=("build", "run"))
