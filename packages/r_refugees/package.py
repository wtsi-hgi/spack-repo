# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefugees(RPackage):
	"""UNHCR Refugee Population Statistics Database

	The Refugee Population Statistics Database published by
    The Office of The United Nations High Commissioner for Refugees (UNHCR)
    contains information about forcibly displaced populations
    spanning more than 70 years of statistical activities.
    It covers displaced populations such as refugees, asylum-seekers and
    internally displaced people, including their demographics.
    Stateless people are also included, most of who have never been displaced.
    The database also reflects the different types of solutions
    for displaced populations such as repatriation or resettlement. 
    More information on the data and methodology can be found on
    the UNHCR Refugee Data Finder <https://www.unhcr.org/refugee-statistics/>.
	"""
	
	homepage = "https://populationstatistics.github.io/refugees/"
	cran = "refugees" 

	version("2023.6.0", md5="f73a763f12acc46dbd090eaed82b885c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble@3.2:", type=("build", "run"))
