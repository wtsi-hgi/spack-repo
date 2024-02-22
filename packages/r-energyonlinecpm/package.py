# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnergyonlinecpm(RPackage):
	"""Distribution Free Multivariate Control Chart Based on Energy
Test

	Provides a function for distribution free control chart based on the change point model, for multivariate statistical process control. The main constituent of the chart is the energy test that focuses on the discrepancy between empirical characteristic functions of two random vectors. This new control chart highlights in three aspects. Firstly, it is distribution free, requiring no knowledge of the random processes. Secondly, this control chart can monitor mean and variance simultaneously. Thirdly it is devised for multivariate time series which is more practical in real data application. Fourthly, it is designed for online detection (Phase II), which is central for real time surveillance of stream data. For more information please refer to O. Okhrin and Y.F. Xu (2017) <https://github.com/YafeiXu/working_paper/raw/master/CPM102.pdf>.
	"""
	
	homepage = "https://sites.google.com/site/EnergyOnlineCPM/"
	cran = "EnergyOnlineCPM" 

	version("1.0", md5="d793aafc7359ef89f2dcbde2520a5d0d")

	depends_on("r-energy", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
