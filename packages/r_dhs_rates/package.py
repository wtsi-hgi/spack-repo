# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDhsRates(RPackage):
	"""Calculates Demographic Indicators

	Calculates key indicators such as fertility rates (Total Fertility Rate (TFR), General Fertility Rate (GFR), 
  and Age Specific Fertility Rate (ASFR)) using Demographic and Health Survey (DHS) women/individual data, 
  childhood mortality probabilities and rates such as Neonatal Mortality Rate (NNMR), Post-neonatal Mortality Rate (PNNMR), 
  Infant Mortality Rate (IMR), Child Mortality Rate (CMR), and Under-five Mortality Rate (U5MR), and adult mortality indicators 
  such as the Age Specific Mortality Rate (ASMR), Age Adjusted Mortality Rate (AAMR), Age Specific Maternal Mortality Rate (ASMMR),
  Age Adjusted Maternal Mortality Rate (AAMMR), Age Specific Pregnancy Related Mortality Rate (ASPRMR), 
  Age Adjusted Pregnancy Related Mortality Rate (AAPRMR), Maternal Mortality Ratio (MMR) and Pregnancy Related Mortality Ratio (PRMR).  
  In addition to the indicators, the 'DHS.rates' package estimates sampling errors indicators such as Standard Error (SE), 
  Design Effect (DEFT), Relative Standard Error (RSE) and Confidence Interval (CI). 
  The package is developed according to the DHS methodology of calculating the fertility indicators and 
  the childhood mortality rates outlined in the 
  "Guide to DHS Statistics" (Croft, Trevor N., Aileen M. J. Marshall, Courtney K. Allen, et al. 2018, <https://dhsprogram.com/Data/Guide-to-DHS-Statistics/index.cfm>) 
  and the DHS methodology of estimating the sampling errors indicators outlined in 
  the "DHS Sampling and Household Listing Manual" (ICF International 2012, <https://dhsprogram.com/pubs/pdf/DHSM4/DHS6_Sampling_Manual_Sept2012_DHSM4.pdf>).
	"""
	
	cran = "DHS.rates" 

	version("0.9.2", md5="f004f1f1fb2c9b26847018dc5c98eae4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
