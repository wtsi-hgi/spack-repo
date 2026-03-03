# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbonds(RPackage):
	"""Rmetrics - Pricing and Evaluating Bonds

	It implements the Nelson-Siegel and the Nelson-Siegel-Svensson
	term structures.
	"""
	
	homepage = "http://www.rmetrics.org"
	cran = "fBonds" 

	version("3042.78", md5="296eb19f16bc492f24b57eabb4ec370f")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
