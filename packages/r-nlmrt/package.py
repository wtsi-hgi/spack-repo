# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlmrt(RPackage):
	"""Functions for Nonlinear Least Squares Solutions

	Replacement for nls() tools for working with nonlinear least squares problems.
      The calling structure is similar to, but much simpler than, that of the nls()
      function. Moreover, where nls() specifically does NOT deal with small or zero
      residual problems, nlmrt is quite happy to solve them. It also attempts to be
      more robust in finding solutions, thereby avoiding 'singular gradient' messages
      that arise in the Gauss-Newton method within nls(). The Marquardt-Nash approach
      in nlmrt generally works more reliably to get a solution, though this may be 
      one of a set of possibilities, and may also be statistically unsatisfactory.
      Added print and summary as of August 28, 2012.
	"""
	
	cran = "nlmrt" 

	version("2016.3.2", md5="dcb183b271103d34fa3c247d195a516b")

	depends_on("r@2.15:", type=("build", "run"))
