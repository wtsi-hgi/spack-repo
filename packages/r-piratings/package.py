# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiratings(RPackage):
	"""Calculate Pi Ratings for Teams Competing in Sport Matches

	Calculate and optimize dynamic performance ratings of association football 
  teams competing in matches, in accordance with the method used in 
  the research paper "Determining the level of ability of football teams by 
  dynamic ratings based on the relative discrepancies in scores between adversaries", 
  by Constantinou and Fenton (2013) 
  <doi:10.1515/jqas-2012-0036>    
  This dynamic rating system has proven to provide superior 
  results for predicting association football outcomes.
	"""
	
	cran = "piratings" 

	version("0.1.9", md5="e240722d25266bdb9f9712f81c725fe4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
