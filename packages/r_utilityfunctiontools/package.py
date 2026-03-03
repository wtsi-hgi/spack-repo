# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtilityfunctiontools(RPackage):
	"""P-Spline Regression for Utility Functions and Derived Measures

	Predicts a smooth and continuous (individual) utility function from utility points, and computes measures of intensity for risk and higher order risk measures (or any other measure computed with user-written function) based on this utility function and its derivatives according to the method introduced in Schneider (2017) <http://hdl.handle.net/21.11130/00-1735-0000-002E-E306-0>.
	"""
	
	homepage = "https://www.sebastianoschneider.com"
	cran = "utilityFunctionTools" 

	version("0.1.1", md5="26128d777f3b4292522a955de4a11721")

	depends_on("r-spatstat-geom", type=("build", "run"))
