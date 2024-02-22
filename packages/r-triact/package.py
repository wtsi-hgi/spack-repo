# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTriact(RPackage):
	"""Analyzing the Lying Behavior of Cows from Accelerometer Data

	Assists in analyzing the lying behavior of cows from raw data 
    recorded with a triaxial accelerometer attached to the hind leg of a cow. Allows 
    the determination of common measures for lying behavior including total lying duration, the 
    number of lying bouts, and the mean duration of lying bouts. Further capabilities are the 
    description of lying laterality and the calculation of proxies for the level of physical 
    activity of the cow. Reference: Simmler M., Brouwers S. P. (2023) <https://gitlab.com/AgroSimi/triact_manuscript>. 
	"""
	
	cran = "triact" 

	version("0.3.0", md5="328a0d48bb3d66edf432b281e08be7e0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-checkmate@2.2:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
