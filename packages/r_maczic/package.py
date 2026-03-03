# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaczic(RPackage):
	"""Mediation Analysis for Count and Zero-Inflated Count Data

	Performs causal mediation analysis for count and zero-inflated
    count data without or with a post-treatment confounder; calculates power
    to detect prespecified causal mediation effects, direct effects, and 
    total effects; performs sensitivity analysis when there is a treatment-
    induced mediator-outcome confounder as described by Cheng, J., Cheng, N.F., 
    Guo, Z., Gregorich, S., Ismail, A.I., Gansky, S.A. (2018) 
    <doi:10.1177/0962280216686131>. Implements Instrumental Variable (IV) 
    method to estimate the controlled (natural) direct and mediation effects, 
    and compute the bootstrap Confidence Intervals as described by Guo, Z., 
    Small, D.S., Gansky, S.A., Cheng, J. (2018) <doi:10.1111/rssc.12233>. This 
    software was made possible by Grant R03DE028410 from the National 
    Institute of Dental and Craniofacial Research, a component of the National 
    Institutes of Health.
	"""
	
	cran = "maczic" 

	version("1.0.0", md5="a76f9d5ac05810de6a7230e1668b9751")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pscl", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mediation", type=("build", "run"))
	depends_on("r-emplik", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
