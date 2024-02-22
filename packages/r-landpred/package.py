# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandpred(RPackage):
	"""Landmark Prediction of a Survival Outcome

	Provides functions for landmark prediction of a survival outcome incorporating covariate and short-term event information. For more information about landmark prediction please see: Parast, Layla, Su-Chun Cheng, and Tianxi Cai. Incorporating short-term outcome information to predict long-term survival with discrete markers. Biometrical Journal 53.2 (2011): 294-307, <doi:10.1002/bimj.201000150>.
	"""
	
	cran = "landpred" 

	version("1.2", md5="26fdca0fca233d5454269cd2eb3ce746")

	depends_on("r-survival", type=("build", "run"))
