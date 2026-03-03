# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimcomp(RPackage):
	"""Simultaneous Comparisons for Multiple Endpoints

	Simultaneous tests and confidence intervals are provided for one-way experimental designs with one or many normally distributed, primary response variables (endpoints). Differences (Hasler and Hothorn, 2011 <doi:10.2202/1557-4679.1258>) or ratios (Hasler and Hothorn, 2012 <doi:10.1080/19466315.2011.633868>) of means can be considered. Various contrasts can be chosen, unbalanced sample sizes are allowed as well as heterogeneous variances (Hasler and Hothorn, 2008 <doi:10.1002/bimj.200710466>) or covariance matrices (Hasler, 2014 <doi:10.1515/ijb-2012-0015>).
	"""
	
	cran = "SimComp" 

	version("3.3", md5="16a0ef779cbad5bb455a7e4e1e3a0883")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-mratios", type=("build", "run"))
