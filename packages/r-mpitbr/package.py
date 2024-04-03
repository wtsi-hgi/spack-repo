# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpitbr(RPackage):
	"""Calculate Alkire-Foster Multidimensional Poverty Measures

	
    Estimate Multidimensional Poverty Indices disaggregated by population subgroups based on the Alkire and Foster method (2011) <doi:10.1016/j.jpubeco.2010.11.006>. This includes the calculation of standard errors and confidence intervals. Other partial indices such as incidence, intensity and indicator-specific measures as well as intertemporal changes analysis can also be estimated. The standard errors and confidence intervals are calculated considering the complex survey design. 
	"""
	
	homepage = "https://github.com/girelaignacio/mpitbR"
	cran = "mpitbR" 

	version("1.0.0", md5="555f2678acb7b8cb542d0ad8999c59ea")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
