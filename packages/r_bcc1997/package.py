# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcc1997(RPackage):
	"""Calculation of Option Prices Based on a Universal Solution

	Calculates the prices of European options based on the universal solution provided by Bakshi, Cao and Chen (1997) <doi:10.1111/j.1540-6261.1997.tb02749.x>. This solution considers stochastic volatility, stochastic interest and random jumps. Please cite their work if this package is used. 
	"""
	
	cran = "BCC1997" 

	version("0.1.1", md5="80a96a8caf90486aaf566058acfc3d15", url="https://cran.r-project.org/src/contrib/BCC1997_0.1.1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
