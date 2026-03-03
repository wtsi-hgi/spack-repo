# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowregenvcost(RPackage):
	"""The Environmental Costs of Flow Regulation

	An application to calculate the daily environmental costs of river flow regulation by dams based on García de Jalon et al. 2017 <doi:10.1007/s11269-017-1663-0>.
	"""
	
	homepage = "https://github.com/garciadejalon/FlowRegEnvCost"
	cran = "FlowRegEnvCost" 

	version("0.1.1", md5="f204de6e2b3cc469c0242f5cc2105f74")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
