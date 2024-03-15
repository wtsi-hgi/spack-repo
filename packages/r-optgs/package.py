# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptgs(RPackage):
	"""Near-Optimal Group-Sequential Designs for Continuous Outcomes

	Optimal group-sequential designs minimise some function of the expected and maximum sample size whilst controlling the type I error rate and power at a specified level. 'OptGS' provides functions to quickly search for near-optimal group-sequential designs for normally distributed outcomes. The methods used are described in Wason, JMS (2015) <doi:10.18637/jss.v066.i02>.
	"""
	
	cran = "OptGS" 

	version("1.2", md5="2eae50924ea31a1f15fe465653aaf778")

