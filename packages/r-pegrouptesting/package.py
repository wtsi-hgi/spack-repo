# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPegrouptesting(RPackage):
	"""Population Proportion Estimation using Group Testing

	The population proportion using group testing can be estimated by different methods. Four functions including p.mle(), p.gart(), p.burrow() and p.order() are provided to implement four estimating methods including the maximum likelihood estimate, Gart's estimate, Burrow's estimate, and order statistic estimate.   
	"""
	
	cran = "PEGroupTesting" 

	version("1.0", md5="4c5342e8516267cbebb03ee7f2c5ba60")

	depends_on("r@3.1:", type=("build", "run"))
