# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKappasize(RPackage):
	"""Sample Size Estimation Functions for Studies of Interobserver
Agreement

	Contains basic tools for sample size estimation in studies of interobserver/interrater agreement (reliability).  Includes functions for both the power-based and confidence interval-based methods, with binary or multinomial outcomes and two through six raters.
	"""
	
	cran = "kappaSize" 

	version("1.2", md5="00e278f7bdca834ee345b485eb860180")

	depends_on("r@2.10:", type=("build", "run"))
