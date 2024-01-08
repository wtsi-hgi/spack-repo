# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RTimeseries(RPackage):
	"""Financial Time Series Objects (Rmetrics)

	'S4' classes and various tools for financial time series:
  Basic functions such as scaling and sorting, subsetting,
  mathematical operations and statistical functions.
	"""
	
	homepage = "https://r-forge.r-project.org/scm/viewvc.php/pkg/timeSeries/?root=rmetrics"
	cran = "timeSeries" 

	version("4031.107", md5="2228b87dd8677eacb2768d3bfa0b65e9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-timedate@2150.95:", type=("build", "run"))
