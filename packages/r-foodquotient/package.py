# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoodquotient(RPackage):
	"""Food Quotient and Nutrient Analysis for HSFFQ

	Aids in analysing data from a food frequency questionnaire known as 
    the Harvard Service Food Frequency Questionnaire (HSFFQ).
    Functions from this package use answers from the HSFFQ to generate 
    estimates of daily consumed micronutrients, calories, macronutrients on 
    an individual level.
    The package also calculates food quotients on individual and group levels. 
    Foodquotient calculation is an often tedious step in the calculation of 
    total human energy expenditure (TEE) using the doubly labeled water method, 
    which is the gold standard for measuring TEE. 
	"""
	
	homepage = "<https://naldc.nal.usda.gov/catalog/32818>"
	cran = "foodquotient" 

	version("0.1.1", md5="a909da054fe080249cb58d084fbde90a")

	depends_on("r@2.10:", type=("build", "run"))
