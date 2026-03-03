# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdf(RPackage):
	"""Estimation and Plotting of IDF Curves

	Intensity-duration-frequency (IDF) curves are a widely used analysis-tool
              in hydrology to assess extreme values of precipitation
              [e.g. Mailhot et al., 2007, <doi:10.1016/j.jhydrol.2007.09.019>].
              The package 'IDF' provides functions to estimate IDF parameters for given
              precipitation time series on the basis of a duration-dependent
              generalized extreme value distribution
              [Koutsoyiannis et al., 1998, <doi:10.1016/S0022-1694(98)00097-3>].
	"""
	
	homepage = "https://gitlab.met.fu-berlin.de/Rpackages/idf_package"
	cran = "IDF" 

	version("2.1.2", md5="d2ad47930c19e392363f43ee0ea397e0")

	depends_on("r-evd", type=("build", "run"))
	depends_on("r-ismev", type=("build", "run"))
	depends_on("r-rcpproll", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
