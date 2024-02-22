# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROreo(RPackage):
	"""Large Amplitude Oscillatory Shear (LAOS)

	The Sequence of Physical Processes (SPP) framework is a way of interpreting the transient data derived from oscillatory rheological tests. It is designed to allow both the linear and non-linear deformation regimes to be understood within a single unified framework. This code provides a convenient way to determine the SPP framework metrics for a given sample of oscillatory data. It will produce a text file containing the SPP metrics, which the user can then plot using their software of choice. It can also produce a second text file with additional derived data (components of tangent, normal, and binormal vectors), as well as pre-plotted figures if so desired. It is the R version of the Package SPP by Simon Rogers Group for Soft Matter (Simon A. Rogers, Brian M. Erwin, Dimitris Vlassopoulos, Michel Cloitre (2011) <doi:10.1122/1.3544591>).
	"""
	
	cran = "oreo" 

	version("1.0", md5="c3c22d789f2264ba61c728bd9efc708b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-spectral", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-fftwtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
