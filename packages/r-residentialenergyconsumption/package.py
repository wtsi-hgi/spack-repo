# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResidentialenergyconsumption(RPackage):
	"""Residential Energy Consumption Data

	Datasets with energy consumption data of different data measurement frequencies. 
    The data stems from several publicly funded research projects of the Chair of Information  
    Systems and Energy Efficient Systems at the University of Bamberg.
	"""
	
	cran = "ResidentialEnergyConsumption" 

	version("1.1.0", md5="11ed883362ea904609443f4106296e6b")

	depends_on("r@3.5:", type=("build", "run"))
