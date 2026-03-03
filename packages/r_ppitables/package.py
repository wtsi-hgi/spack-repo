# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpitables(RPackage):
	"""Lookup Tables to Generate Poverty Likelihoods and Rates using
the Poverty Probability Index (PPI)

	The Poverty Probability Index (PPI) is a poverty measurement tool 
    for organizations and businesses with a mission to serve the poor. The PPI 
    is statistically-sound, yet simple to use: the answers to 10 questions about 
    a household’s characteristics and asset ownership are scored to compute the 
    likelihood that the household is living below the poverty line – or above by 
    only a narrow margin. This package contains country-specific lookup data tables
    used as reference to determine the poverty likelihood of a household based
    on their score from the country-specific PPI questionnaire. These lookup 
    tables have been extracted from documentation of the PPI found at 
    <https://www.povertyindex.org> and managed by Innovations for Poverty Action 
    <https://www.poverty-action.org>.
	"""
	
	homepage = "https://github.com/katilingban/ppitables"
	cran = "ppitables" 

	version("0.5.4", md5="0d0586873cc9f9f76d98cd48c0608dc5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
