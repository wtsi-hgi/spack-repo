# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdsopt(RPackage):
	"""Searching for Optimal MDS Procedure for Metric and
Interval-Valued Data

	Selecting the optimal multidimensional scaling (MDS) procedure for metric data via metric MDS (ratio, interval, mspline) and nonmetric MDS (ordinal). Selecting the optimal multidimensional scaling (MDS) procedure for interval-valued data via metric MDS (ratio, interval, mspline).Selecting the optimal multidimensional scaling procedure for interval-valued data by varying all combinations of normalization and optimization methods.Selecting the optimal MDS procedure for statistical data referring to the evaluation of tourist attractiveness of Lower Silesian counties.
 (Borg, I., Groenen, P.J.F., Mair, P. (2013) <doi:10.1007/978-3-642-31848-1>, 
 Walesiak, M. (2016) <doi:10.15611/ekt.2016.2.01>, 
 Walesiak, M. (2017) <doi:10.15611/ekt.2017.3.01>).
	"""
	
	cran = "mdsOpt" 

	version("0.7-6", md5="f3e4aa9ff43b57cba6c2706ba41c3bb2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-smacof", type=("build", "run"))
	depends_on("r-clustersim", type=("build", "run"))
	depends_on("r-symbolicda", type=("build", "run"))
	depends_on("r-animation", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
