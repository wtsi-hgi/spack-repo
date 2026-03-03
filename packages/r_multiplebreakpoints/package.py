# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiplebreakpoints(RPackage):
	"""Estimating Multiple Breakpoints for a Sequence of Realizations
of Bernoulli Variables

	The iterative procedure estimates structural changes in the success probability of Bernoulli variables. It estimates the number and location of the breakpoints as well as the success probability of the different sequences between the breakpoints. In addition, it provides a graphical illustration of the result.
	"""
	
	cran = "MultipleBreakpoints" 

	version("0.1.0", md5="02835003ccc7a26296557b7deacf1f17")

	depends_on("r-rdpack", type=("build", "run"))
