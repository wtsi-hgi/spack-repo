# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcnetmeta(RPackage):
	"""Patient-Centered Network Meta-Analysis

	Performs Bayesian arm-based network meta-analysis for datasets with binary, continuous, and count outcomes
 (Zhang et al., 2014 <doi:10.1177/1740774513498322>;
  Lin et al., 2017 <doi:10.18637/jss.v080.i05>).
	"""
	
	cran = "pcnetmeta" 

	version("2.8", md5="e79ad340b96375ff280730ccd4e7b603")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("jags@4.0.0:4.999.999", type=("build", "link", "run"))
