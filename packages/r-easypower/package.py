# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasypower(RPackage):
	"""Sample Size Estimation for Experimental Designs

	Power analysis is used in the estimation of sample sizes for
    experimental designs. Most programs and R packages will only output the highest
    recommended sample size to the user. Often the user input can be complicated
    and computing multiple power analyses for different treatment comparisons can
    be time consuming. This package simplifies the user input and allows the user
    to view all of the sample size recommendations or just the ones they want to see.
    The calculations used to calculate the recommended sample sizes are from the
    'pwr' package.
	"""
	
	cran = "easypower" 

	version("1.0.1", md5="dbe044eaeebf952a37bdb399caafdfd8")

	depends_on("r-pwr@1.1.3:", type=("build", "run"))
