# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulteq(RPackage):
	"""Multiple Equivalence Tests and Simultaneous Confidence Intervals

	Equivalence tests and related confidence intervals for the
 comparison of two treatments, simultaneously for one or many normally
 distributed, primary response variables (endpoints). The step-up
 procedure of Quan et al. (2001) is both applied for differences and
 extended to ratios of means. A related single-step procedure is also
 available.
	"""
	
	cran = "MultEq" 

	version("2.4", md5="4b25a646a5571e382afc5318ccd93d83")

	depends_on("r@2.10:", type=("build", "run"))
