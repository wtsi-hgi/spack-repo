# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArse(RPackage):
	"""Area of Resilience to Stress Event

	A method for quantifying resilience after a stress event. A set of functions
    calculate the area of resilience that is created by the departure of baseline 
    'y' (i.e., robustness) and the time taken 'x' to return to baseline 
    (i.e., rapidity) after a stress event using the Cartesian coordinates of the 
    data. This package has the capability to calculate areas of resilience,
    growth, and cases in which resilience is not achieved 
    (e.g., diminished performance without return to baseline).
	"""
	
	homepage = "https://github.com/nr3xe/arse"
	cran = "arse" 

	version("1.0.0", md5="ad13c6e56065903ab5c1ebf6b45f7eed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
