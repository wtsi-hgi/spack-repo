# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdhonest(RPackage):
	"""Honest Inference in Regression Discontinuity Designs

	Honest and nearly-optimal confidence intervals in fuzzy and sharp
    regression discontinuity designs and for inference at a point based on local
    linear regression. The implementation is based on Armstrong and Kolesár (2018)
    <doi:10.3982/ECTA14434>, and Kolesár and Rothe (2018)
    <doi:10.1257/aer.20160945>. Supports covariates, clustering, and weighting.
	"""
	
	homepage = "https://github.com/kolesarm/RDHonest"
	cran = "RDHonest" 

	version("1.0.0", md5="3003b43a359e4c05aa817d5f288e8d92")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
