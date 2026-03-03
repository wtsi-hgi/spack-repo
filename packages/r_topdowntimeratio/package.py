# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopdowntimeratio(RPackage):
	"""Top-Down Time Ratio Segmentation for Coordinate Trajectories

	Data collected on movement behavior is often in the form of time-
    stamped latitude/longitude coordinates sampled from the underlying movement
    behavior. These data can be compressed into a set of segments via the Top-
    Down Time Ratio Segmentation method described in Meratnia and de By (2004)
    <doi:10.1007/978-3-540-24741-8_44> which, with some loss of information, 
    can both reduce the size of the data as well as provide corrective smoothing
    mechanisms to help reduce the impact of measurement error.  This is an
    improvement on the well-known Douglas-Peucker algorithm for segmentation
    that operates not on the basis of perpendicular distances. Top-Down Time
    Ratio segmentation allows for disparate sampling time intervals by
    calculating the distance between locations and segments with respect to
    time. Provided a trajectory with timestamps, tdtr() returns a set of straight-
    line segments that can represent the full trajectory. McCool, Lugtig,
    and Schouten (2022) <doi:10.1007/s11116-022-10328-2> describe this method as
    implemented here in more detail. 
	"""
	
	cran = "topdowntimeratio" 

	version("0.1.0", md5="1e919f53b82e2aa15d6f2d78194aba3f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-geodist@0.0.4:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
