# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlmdatadriven(RPackage):
	"""Robust Regression with Data Driven Tuning Parameter

	Data driven approach for robust regression estimation in homoscedastic and heteroscedastic context. See Wang et al. (2007), <doi:10.1198/106186007X180156> regarding homoscedastic framework.  
	"""
	
	cran = "rlmDataDriven" 

	version("0.4.0", md5="b4ef5e05b10ecdf636f37c8b5def38c1")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
