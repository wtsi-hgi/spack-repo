# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSftrack(RPackage):
	"""Modern Classes for Tracking and Movement Data

	Modern classes for tracking and movement data, building
    on 'sf' spatial infrastructure, and early theoretical work from
    Turchin (1998, ISBN: 9780878938476), and Calenge et al. (2009)
    <doi:10.1016/j.ecoinf.2008.10.002>. Tracking data are series of
    locations with at least 2-dimensional spatial coordinates (x,y), a
    time index (t), and individual identification (id) of the object
    being monitored; movement data are made of trajectories, i.e. the
    line representation of the path, composed by steps (the
    straight-line segments connecting successive locations). 'sftrack'
    is designed to handle movement of both living organisms and
    inanimate objects.
	"""
	
	homepage = "https://mablab.org/sftrack/"
	cran = "sftrack" 

	version("0.5.4", md5="c7c5b45ad63d1b19583d6ad2b5884d4c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
