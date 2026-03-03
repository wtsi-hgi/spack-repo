# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestinventory(RPackage):
	"""Design-Based Global and Small-Area Estimations for Multiphase
Forest Inventories

	Extensive global and small-area estimation procedures for multiphase
    forest inventories under the design-based Monte-Carlo approach are provided.
    The implementation has been published in the Journal of Statistical Software (<doi:10.18637/jss.v097.i04>) 
    and includes estimators for simple and cluster sampling
    published by Daniel Mandallaz in 2007 (<doi:10.1201/9781584889779>),
    2013 (<doi:10.1139/cjfr-2012-0381>, <doi:10.1139/cjfr-2013-0181>,
    <doi:10.1139/cjfr-2013-0449>, <doi:10.3929/ethz-a-009990020>)
    and 2016 (<doi:10.3929/ethz-a-010579388>). It provides point estimates,
    their external- and design-based variances and confidence intervals, as well as a
    set of functions to analyze and visualize the produced estimates.
    The procedures have also been optimized for the use of remote sensing data
    as auxiliary information, as demonstrated in 2018 by Hill et al. (<doi:10.3390/rs10071052>).
	"""
	
	cran = "forestinventory" 

	version("1.0.0", md5="183d5c391a33b542cc1328ab3e05b537")

	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
