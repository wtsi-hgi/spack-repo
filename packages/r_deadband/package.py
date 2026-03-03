# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeadband(RPackage):
	"""Statistical Deadband Algorithms Comparison

	Statistical deadband algorithms are based on the Send-On-Delta concept as in Miskowicz(2006,<doi:10.3390/s6010049>). A collection of functions compare effectiveness and fidelity of sampled signals using statistical deadband algorithms.
	"""
	
	cran = "deadband" 

	version("0.1.0", md5="dfef4c2b8448860febe6a85f532df677")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
