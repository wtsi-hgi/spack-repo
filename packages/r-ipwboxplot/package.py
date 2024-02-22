# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpwboxplot(RPackage):
	"""Adapted Boxplot to Missing Observations

	Boxplots adapted to the happenstance of missing observations where drop-out probabilities can be given by the practitioner or  modelled  using auxiliary covariates. The paper of "Zhang, Z., Chen, Z., Troendle, J. F. and Zhang, J.(2012) <doi:10.1111/j.1541-0420.2011.01712.x>", proposes estimators of marginal quantiles based on the Inverse Probability Weighting method.
	"""
	
	cran = "IPWboxplot" 

	version("0.1.2", md5="23d145bb1d2b0d7cf0dfdfe5e55d7251")

	depends_on("r-isotone", type=("build", "run"))
