# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStplanr(RPackage):
	"""Sustainable Transport Planning

	Tools for transport planning with an emphasis on spatial
    transport data and non-motorized modes. Create geographic "desire
    lines" from origin-destination (OD) data (building on the 'od'
    package); calculate routes on the transport network locally and via
    interfaces to routing services such as <https://cyclestreets.net/>;
    calculate route segment attributes such as bearing.  The package
    implements the 'travel flow aggregration' method described in Morgan
    and Lovelace (2020) <doi:10.1177/2399808320942779>.  Further
    information on the package's aim and scope can be found in the
    vignettes and in a paper in the R Journal (Lovelace and Ellison 2018)
    <doi:10.32614/RJ-2018-053>.
	"""
	
	homepage = "https://github.com/ropensci/stplanr"
	cran = "stplanr" 

	version("1.1.2", md5="42a07fd09627edac5575f8d0e10c7359")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-lwgeom@0.1.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nabor@0.5:", type=("build", "run"))
	depends_on("r-od", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp@0.12.1:", type=("build", "run"))
	depends_on("r-rlang@0.2.2:", type=("build", "run"))
	depends_on("r-sf@0.6.3:", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
