# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterses(RPackage):
	"""Calculate Cluster-Robust p-Values and Confidence Intervals

	Calculate p-values and confidence intervals using cluster-adjusted
    t-statistics (based on Ibragimov and Muller (2010) <DOI:10.1198/jbes.2009.08046>, pairs cluster bootstrapped t-statistics, and wild cluster bootstrapped t-statistics (the latter two techniques based on Cameron, Gelbach, and Miller (2008) <DOI:10.1162/rest.90.3.414>. Procedures are included for use with GLM, ivreg, plm (pooling or fixed effects), and mlogit models.
	"""
	
	cran = "clusterSEs" 

	version("2.6.5", md5="5ab8521a1769708cbd96f037be4f62de")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mlogit@1.1.0:", type=("build", "run"))
	depends_on("r-dfidx", type=("build", "run"))
