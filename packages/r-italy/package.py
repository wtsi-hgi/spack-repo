# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItaly(RPackage):
	"""The Italian Survey on Household and Wealth, 2008 and 2010

	Provides two record linkage data sets on the Italian Survey on Household and Wealth, 2008 and 2010, a sample survey conducted by the Bank of Italy every two years. The 2010 survey covered 13,702 individuals, while the 2008 survey covered 13,734 individuals. The following categorical variables are included in this data set: year of birth, working status, employment status, branch of activity, town size, geographical area of birth, sex, whether or not Italian national, and highest educational level obtained. Unique identifiers are available to assess the accuracy of one’s method. Please see Steorts (2015) <DOI:10.1214/15-BA965SI> to find more details about the data set. 
	"""
	
	cran = "italy" 

	version("0.1.0", md5="766c41e359621bcfe60c60c9bf677467")

	depends_on("r@3.3.1:", type=("build", "run"))
