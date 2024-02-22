# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoweatherindices(RPackage):
	"""Calculating Weather Indices

	Weather indices are formed from weather variables in this package. The users can input any number of weather variables recorded over any number of weeks. This package has no restriction on the number of weeks and weather variables to be taken as input.The details of the method can be seen (i)'Joint effects of weather variables on rice yields' by  R. Agrawal, R. C. Jain  and M. P. Jha in Mausam, vol. 34, pp. 189-194, 1983,<doi:10.54302/mausam.v34i2.2392>,(ii)'Improved weather indices based Bayesian regression model for forecasting crop yield' by  M. Yeasin, K. N. Singh, A. Lama and B. Gurung in Mausam, vol. 72, pp.879-886, 2021,<doi:10.54302/mausam.v72i4.670>.
	"""
	
	cran = "AutoWeatherIndices" 

	version("0.1.0", md5="c34203f0b362e5d91c88f1191e696a00")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
