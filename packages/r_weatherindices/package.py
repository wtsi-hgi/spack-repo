# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeatherindices(RPackage):
	"""Calculate Weather Indices

	Weather indices represent the overall weekly effect of a weather variable on crop yield throughout the cropping season. This package contains functions that can convert the weekly weather data into yearly weighted Weather indices with weights being the correlation coefficient between weekly weather data over the years and crop yield over the years. This can be done for an individual weather variable and for two weather variables at a time as the interaction effect. This method was first devised by Jain, RC, Agrawal R, and Jha, MP (1980), "Effect of climatic variables on rice yield and its forecast",MAUSAM, 31(4), 591–596, <doi:10.54302/mausam.v31i4.3477>. Later, the method have been used by various researchers and the latest can found in Gupta, AK, Sarkar, KA, Dhakre, DS, & Bhattacharya, D (2022), "Weather Based Potato Yield Modelling using Statistical and Machine Learning Technique",Environment and Ecology, 40(3B), 1444–1449,<https://www.environmentandecology.com/volume-40-2022>.
	"""
	
	cran = "weatherindices" 

	version("0.1.0", md5="40a7fb4920049aedd2bedf67cd96d04e")

	depends_on("r@2.10:", type=("build", "run"))
