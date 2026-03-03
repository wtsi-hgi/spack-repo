# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCotrend(RPackage):
	"""Consistent Co-Trending Rank Selection

	Implements cointegration/co-trending rank selection
        algorithm in Guo and Shintani (2013) "Consistent
        co-trending rank selection when both stochastic and nonlinear
        deterministic trends are present". 
        The Econometrics Journal 16: 473-483 
        <doi:10.1111/j.1368-423X.2012.00392.x>.
        Numbered examples correspond to Feb 2011 preprint 
        <http://www.fas.nus.edu.sg/ecs/events/seminar/seminar-papers/05Apr11.pdf>.
	"""
	
	cran = "cotrend" 

	version("1.0.2", md5="e01e8d042841cb1ad77e6dbe5d332801")

	depends_on("r-xts", type=("build", "run"))
