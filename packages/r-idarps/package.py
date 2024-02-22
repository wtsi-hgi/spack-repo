# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdarps(RPackage):
	"""Datasets and Functions for the Class "Modelling and Data
Analysis for Pharmaceutical Sciences"

	Provides datasets and functions for the class "Modelling and Data Analysis for Pharmaceutical Sciences". 
             The datasets can be used to present various methods of data analysis and statistical modeling.
             Functions for data visualization are also implemented. 
	"""
	
	cran = "idarps" 

	version("0.0.3", md5="97c19eb5e074d841122861a13edc377d")

	depends_on("r@3.5:", type=("build", "run"))
