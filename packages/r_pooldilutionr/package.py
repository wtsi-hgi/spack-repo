# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPooldilutionr(RPackage):
	"""Calculate Gross Biogeochemical Flux Rates from Isotope Pool
Dilution Data

	Pool dilution is a isotope tracer technique wherein a 
    biogeochemical pool is artifically enriched with its heavy isotopologue 
    and the gross productive and consumptive fluxes of that pool are 
    quantified by the change in pool size and isotopic composition over time. 
    This package calculates gross production and consumption rates from
    closed-system isotopic pool dilution time series data. Pool size 
    concentrations and heavy isotope (e.g., 15N) content are measured over time 
    and the model optimizes production rate (P) and the first order rate 
    constant (k) by minimizing error in the model-predicted total pool size, 
    as well as the isotopic signature. The model optimizes rates by weighting 
    information against the signal:noise ratio of concentration and heavy-
    isotope signatures using measurement precision as well as the magnitude of 
    change over time. The calculations used here are based on von Fischer and 
    Hedin (2002) <doi:10.1029/2001GB001448> with some modifications.
	"""
	
	cran = "PoolDilutionR" 

	version("1.0.0", md5="4044ef63319a03c6d795bc3d6cfcdf87")

	depends_on("r@2.10:", type=("build", "run"))
