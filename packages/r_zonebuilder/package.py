# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZonebuilder(RPackage):
	"""Create and Explore Geographic Zoning Systems

	Functions, documentation and example data to help divide
    geographic space into discrete polygons (zones).
    The functions are motivated by research into the merits of different zoning systems
    <doi:10.1068/a090169>. A flexible 'ClockBoard' zoning system is
    provided, which breaks-up space by concentric rings
    and radial lines emanating from a central point.
    By default, the diameter of the rings grow according the triangular number sequence
    <doi:10.1080/26375451.2019.1598687> with the first 4 'doughnuts'
    (or 'annuli') measuring 1, 3, 6, and 10 km wide.
    These annuli are subdivided into equal segments (12 by default), creating the
    visual impression of a dartboard. Zones are labelled according to
    distance to the centre and angular distance from North, creating a simple
    geographic zoning and labelling system useful for visualising geographic
    phenomena with a clearly demarcated central location such as cities.
	"""
	
	homepage = "https://github.com/zonebuilders/zonebuilder"
	cran = "zonebuilder" 

	version("0.0.2", md5="eb498a4b9f6bc063d90672617d0bd414")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
