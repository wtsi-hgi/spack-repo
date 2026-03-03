# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVolleystat(RPackage):
	"""Detailed Statistics on Volleyball Matches

	Volleyball match statistics of the German volleyball first division league (seasons 2013/2014 to 
    2018/2019). The data has been collected from the official volleyball first division homepage 
    (<www.volleyball-bundesliga.de>) and contains information on teams, staff, sets, matches, and player-in-match 
    statistics (extracted automatically from the official match reports).
	"""
	
	homepage = "http://github.com/bozhinvi/volleystat"
	cran = "volleystat" 

	version("0.2.0", md5="98892e6eca7ca540bde8283c8e05ac1f")

	depends_on("r@2.10:", type=("build", "run"))
