# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrhawkes(RPackage):
	"""Multivariate Renewal Hawkes Process

	Simulate a (bivariate) multivariate renewal Hawkes (MRHawkes) 
    self-exciting process, with given immigrant hazard rate functions and 
    offspring density function. Calculate the likelihood of a MRHawkes process 
    with given hazard rate functions and offspring density function for an 
    (increasing) sequence of event times. Calculate the Rosenblatt residuals of the 
    event times. Predict future event times based on observed event times up to a 
    given time. For details see Stindl and Chen (2018) <doi:10.1016/j.csda.2018.01.021>.
	"""
	
	cran = "MRHawkes" 

	version("1.0", md5="a898af3853c12c5597cddf81c29bd44b")

	depends_on("r-ihsep", type=("build", "run"))
