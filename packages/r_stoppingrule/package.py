# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStoppingrule(RPackage):
	"""Create and Evaluate Stopping Rules for Safety Monitoring

	Provides functions for creating, displaying, and evaluating stopping rules for safety monitoring in clinical studies. Implements stopping rule methods described in Goldman (1987) <doi:10.1016/0197-2456(87)90153-X>; Geller et al. (2003, ISBN:9781135524388); Ivanova, Qaqish, and Schell (2005) <doi:10.1111/j.1541-0420.2005.00311.x>; Chen and Chaloner (2006) <doi:10.1002/sim.2429>; and Kulldorff et al. (2011) <doi:10.1080/07474946.2011.539924>.
	"""
	
	cran = "stoppingrule" 

	version("0.4.0", md5="13e76a7175a20fc4f7d86bcd95b24d9a")
	version("0.3.0", md5="a71cf1944e09e93f891b5d5206b47472")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
