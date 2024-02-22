# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrectedauc(RPackage):
	"""Correcting AUC for Measurement Error

	Correcting area under ROC (AUC) for measurement error based on probit-shift model.
	"""
	
	cran = "correctedAUC" 

	version("0.0.3", md5="5c41df70e082b300dc23cce7bc020790")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-icc", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
