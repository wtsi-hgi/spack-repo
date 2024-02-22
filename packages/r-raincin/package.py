# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaincin(RPackage):
	"""Ranking with Incomplete Information

	Various statistical and mathematical ranking and rating methods with incomplete information are included. This package is initially designed for the scoring system in a high school project showcase to rank student research projects, where each judge can only evaluate a set of projects in a limited time period. See Langville, A. N. and Meyer, C. D. (2012), Who is Number 1: The Science of Rating and Ranking, Princeton University Press <doi:10.1515/9781400841677>, and Gou, J. and Wu, S. (2020), A Judging System for Project Showcase: Rating and Ranking with Incomplete Information, Technical Report.
	"""
	
	cran = "raincin" 

	version("1.0.3", md5="adc657d648af689bbfb12527f99556ba")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-popdemo", type=("build", "run"))
