# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMortalitygaps(RPackage):
	"""The Double-Gap Life Expectancy Forecasting Model

	Life expectancy is highly correlated over time among countries and 
  between males and females. These associations can be used to improve forecasts. 
  Here we have implemented a method for forecasting female life expectancy based on 
  analysis of the gap between female life expectancy in a country compared with
  the record level of female life expectancy in the world. Second, to forecast 
  male life expectancy, the gap between male life expectancy and female life 
  expectancy in a country is analysed. We named this method the Double-Gap model.
  For a detailed description of the method see Pascariu et al. (2017). 
  <doi:10.1016/j.insmatheco.2017.09.011>.
	"""
	
	homepage = "https://github.com/mpascariu/MortalityGaps"
	cran = "MortalityGaps" 

	version("1.0.0", md5="4d638346530fb267776db6d9038a853c")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-crch", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
