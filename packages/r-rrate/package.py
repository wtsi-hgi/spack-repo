# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrate(RPackage):
	"""Estimating Replication Rate for Genome-Wide Association Studies

	Replication Rate (RR) is the probability of replicating a statistically significant association in genome-wide association studies. This R-package provide the estimation method for replication rate which makes use of the summary statistics from the primary study. We can use the estimated RR to determine the sample size of the replication study, and to check the consistency between the results of the primary study and those of the replication study.
	"""
	
	cran = "RRate" 

	version("1.0", md5="8921cec66971131b1f9b92d3775e5480")

	depends_on("r@2.10:", type=("build", "run"))
