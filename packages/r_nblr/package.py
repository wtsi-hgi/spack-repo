# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNblr(RPackage):
	"""Data Extraction of Australian NBL Basketball Statistics

	Allow users to obtain basketball statistics for 
    the Australian basketball league 'NBL'<https://nbl.com.au/>. 
    Stats include play-by-play, shooting locations, results and 
    box scores for teams and players.
	"""
	
	homepage = "https://github.com/JaseZiv/nblR"
	cran = "nblR" 

	version("0.0.4", md5="a43032ff6c2874e56e1183a482d370d8")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
