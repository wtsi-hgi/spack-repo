# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSteppedpower(RPackage):
	"""Power Calculation for Stepped Wedge Designs

	Tools for power and sample size 
    calculation as well as design diagnostics for 
    longitudinal mixed model settings, with a focus on stepped wedge designs.
    All calculations are oracle estimates i.e. assume random effect variances 
    to be known (or guessed) in advance.  
    The method is introduced in Hussey and Hughes (2007) <doi:10.1016/j.cct.2006.05.007>,
    extensions are discussed in Li et al. (2020) <doi:10.1177/0962280220932962>.
	"""
	
	cran = "SteppedPower" 

	version("0.3.4", md5="a6a64aca162ce17b7124f8236d32bf94")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
