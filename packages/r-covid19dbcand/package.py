# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovid19dbcand(RPackage):
	"""Selected 'Drugbank' Drugs for COVID-19 Treatment Related Data in
R Format

	Provides different datasets parsed from 'Drugbank' 
    <https://www.drugbank.ca/covid-19> database using 'dbparser' package. 
    It is a smaller version from 'dbdataset' package. It contains only information
    about COVID-19 possible treatment.
	"""
	
	homepage = "https://github.com/MohammedFCIS/covid19dbcand"
	cran = "covid19dbcand" 

	version("0.1.1", md5="be5633664da232ae9a1361c2c9ca0a8f")

	depends_on("r@3.1:", type=("build", "run"))
