# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiogas(RPackage):
	"""Process Biogas Data and Predict Biogas Production

	High- and low-level functions for processing biogas data and predicting biogas production. Molar mass and calculated oxygen demand (COD') can be determined from a chemical formula. Measured gas volume can be corrected for water vapor and to (possibly user-defined) standard temperature and pressure. Gas quantity can be converted between volume, mass, and moles. Gas composition, cumulative production, or other variables can be interpolated to a specified time. Cumulative biogas and methane production (and rates) can be calculated using volumetric, manometric, gravimetric, or gas density methods for any number of bottles. With cumulative methane production data and data on bottle contents, biochemical methane potential (BMP) can be calculated and summarized, including subtraction of the inoculum contribution and normalization by substrate mass. Cumulative production and production rates can be summarized in several different ways (e.g., omitting normalization) using the same function. Biogas quantity and composition can be predicted from substrate composition and additional, optional data. Lastly, inoculum and substrate mass can be determined for planning BMP experiments.
	"""
	
	cran = "biogas" 

	version("1.23.2", md5="a5011e46785ab49f8e99e17b422b7c2c")

