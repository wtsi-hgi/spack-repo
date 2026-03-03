# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS2dverification(RPackage):
	"""Set of Common Tools for Forecast Verification

	Set of tools to verify forecasts through the computation of typical
    prediction scores against one or more observational datasets or reanalyses (a
    reanalysis being a physical extrapolation of observations that relies on the
    equations from a model, not a pure observational dataset). Intended for seasonal
    to decadal climate forecasts although can be useful to verify other kinds of
    forecasts. The package can be helpful in climate sciences for other purposes
    than forecasting. To find more details, see the review paper Manubens, N.et al. (2018)
    <doi:10.1016/j.envsoft.2018.01.018>.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/s2dverification/-/wikis/home"
	cran = "s2dverification" 

	version("2.10.3", md5="8e1ab9208527c3a2385ebf22b0a472ed")

	depends_on("r-maps", type=("build", "run"))
	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-geomap", type=("build", "run"))
	depends_on("r-geomapdata", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-specsverification@0.5:", type=("build", "run"))
