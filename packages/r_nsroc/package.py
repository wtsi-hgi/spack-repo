# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNsroc(RPackage):
	"""Non-Standard ROC Curve Analysis

	Tools for estimating Receiver Operating Characteristic (ROC) curves,
        building confidence bands, comparing several curves both for dependent and 
        independent data, estimating the cumulative-dynamic ROC curve in presence of
        censored data, and performing meta-analysis studies, among others.
	"""
	
	cran = "nsROC" 

	version("1.1", md5="99d2eb7dab15f77090f44a32efc6785c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sde", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
