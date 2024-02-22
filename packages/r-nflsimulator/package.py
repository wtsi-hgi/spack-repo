# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflsimulator(RPackage):
	"""Simulating Plays and Drives in the NFL

	The intent here is to enable the simulation of plays/drives and
    evaluate game-play strategies in the National Football League (NFL).
    Built-in strategies include going for it on fourth down and varying the 
    proportion of passing/rushing plays during a drive. The user should be
    familiar with nflscrapR data before trying to write his/her own 
    strategies. This work is inspired by a blog post by Mike Lopez, 
    currently the  Director of Data and Analytics at the NFL, Lopez (2019) <https://statsbylopez.netlify.app/post/resampling-nfl-drives/>.
	"""
	
	homepage = "https://github.com/rtelmore/NFLSimulatoR/"
	cran = "NFLSimulatoR" 

	version("0.4.0", md5="077d17b279dc56828753d806db278e48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-nflfastr", type=("build", "run"))
