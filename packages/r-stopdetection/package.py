# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStopdetection(RPackage):
	"""Stop Detection in Timestamped Trajectory Data using
Spatiotemporal Clustering

	Trajectory data formed by human or animal movement is often marked 
    by periods of movement interspersed with periods of standing still. It is
    often of interest to researchers to separate geolocation trajectories of
    latitude/longitude points by clustering consecutive locations to produce a
    model of this behavior. This package implements the Stay Point detection
    algorithm originally described in Ye (2009) <doi:10.1109/MDM.2009.11> that
    uses time and distance thresholds to characterize spatial regions as
    'stops'. This package also implements the concept of merging described in
    Montoliu (2013) <doi:10.1007/s11042-011-0982-z> as stay point region
    estimation, which allows for clustering of temporally adjacent stops for
    which distance between the midpoints is less than the provided threshold.
    GPS-like data from various sources can be used, but the temporal thresholds
    must be considered with respect to the sampling interval, and the spatial 
    thresholds must be considered with respect to the measurement error.
	"""
	
	homepage = "https://github.com/daniellemccool/stopdetection"
	cran = "stopdetection" 

	version("0.1.2", md5="6fde96fe11d1f5d86623c83e3ecf8826")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
