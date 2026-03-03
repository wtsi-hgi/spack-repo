# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartmeteranalytics(RPackage):
	"""Methods for Smart Meter Data Analysis

	Methods for analysis of energy consumption data (electricity, gas, 
    water) at different data measurement intervals. The package provides feature extraction 
    methods and algorithms to prepare data for data mining and machine learning 
    applications. Deatiled descriptions of the methods and their application can be found 
    in Hopf (2019, ISBN:978-3-86309-669-4) "Predictive Analytics for Energy Efficiency and 
    Energy Retailing" <doi:10.20378/irbo-54833> and Hopf et al. (2016) <doi:10.1007/s12525-018-0290-9> 
    "Enhancing energy efficiency in the residential sector with smart meter data analytics".
	"""
	
	cran = "SmartMeterAnalytics" 

	version("1.0.3", md5="d48f8a506522e9166b211df94c8aeb65")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-stinepack", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
