# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrowr(RPackage):
	"""Implementation of the Vegetation Model ModVege

	Run grass growth simulations using a grass growth model based 
    on ModVege (Jouven, M., P. Carrère, and R. Baumont "Model Predicting 
    Dynamics of Biomass, Structure and Digestibility of Herbage in Managed 
    Permanent Pastures. 1. Model Description." (2006) 
    <doi:10.1111/j.1365-2494.2006.00515.x>). The implementation in
    this package contains a few additions to the above cited version of ModVege,
    such as simulations of management decisions, and influences of snow cover.
    As such, the model is fit to simulate grass growth in mountainous 
    regions, such as the Swiss Alps. The package also contains routines for 
    calibrating the model and helpful tools for analysing model outputs and 
    performance.
	"""
	
	homepage = "https://github.com/kuadrat/growR"
	cran = "growR" 

	version("1.2.0", md5="3738a303189e11556f7d6e229853bd22")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
