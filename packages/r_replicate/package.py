# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReplicate(RPackage):
	"""Statistical Metrics for Multisite Replication Studies

	For a multisite replication project, computes the consistency metric P_orig, which is
    the probability that the original study would observe an estimated effect size as extreme or more extreme
    than it actually did, if in fact the original study were statistically consistent with the replications. Other
    recommended metrics are: (1) the probability of a true effect of scientifically meaningful size in the same direction as the estimate
    the original study; and (2) the probability of a true effect of meaningful size in the direction opposite
    the original study's estimate. These two can be computed using the package code{MetaUtility::prop_stronger}.
    Additionally computes older metrics used in replication projects (namely expected agreement in "statistical significance" between an original study and replication studies as well
    as prediction intervals for the replication estimates). See Mathur and VanderWeele (under review; <https://osf.io/apnjk/>)
    for details. 
	"""
	
	cran = "Replicate" 

	version("1.2.0", md5="2d89cbca1246a632be39672bb92d0600")

	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
