# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REufootball(RPackage):
	"""Football Match Data of European Leagues

	Contains match results from seven European men's football leagues, namely Premier League (England), Ligue 1 (France), 
	     Bundesliga (Germany), Serie A (Italy), Primera Division (Spain), Eredivisie (The Netherlands), Super Lig (Turkey).
	     Includes Seasons 2010/2011 until 2019/2020 and a set of interesting covariates. Can be used all purposes.
	"""
	
	cran = "EUfootball" 

	version("0.0.1", md5="04726521ddfa10a251b1f9ded6c9e91b")

	depends_on("r@3.5:", type=("build", "run"))
