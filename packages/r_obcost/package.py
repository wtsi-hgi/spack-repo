# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObcost(RPackage):
	"""Obesity Cost Database

	This database contains necessary data relevant to medical costs on obesity throughout the United States. This database, in form of an R package, could output necessary data frames relevant to obesity costs, where the clients could easily manipulate the output using difference parameters, e.g. relative risks for each illnesses. This package contributes to parts of our published journal named "Modeling the Economic Cost of Obesity Risk and Its Relation to the Health Insurance Premium in the United States: A State Level Analysis". Please use the following citation for the journal: Woods Thomas, Tatjana Miljkovic (2022) "Modeling the Economic Cost of Obesity Risk and Its Relation to the Health Insurance Premium in the United States: A State Level Analysis" <doi:10.3390/risks10100197>. The database is composed of the following main tables: 1. Relative_Risks: (constant) Relative risks for a given disease group with a risk factor of obesity; 2. Disease_Cost: (obesity_cost_disease) Supplementary output with all variables related to individual disease groups in a given state and year; 3. Full_Cost: (obesity_cost_full) Complete output with all variables used to make cost calculations, as well as cost calculations in a given state and year; 4. National_Summary: (obesity_cost_national_summary) National summary cost calculations in a given year. Three functions are included to assist users in calling and adjusting the mentioned tables and they are data_load(), data_produce(), and rel_risk_fun(). 
	"""
	
	cran = "obcost" 

	version("0.1.0", md5="9bd6df0dcefb2544d64347bd6ad315f6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
