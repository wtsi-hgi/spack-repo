# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtide(RPackage):
	"""Tide Heights

	Calculates tide heights based on tide station harmonics.  It
    includes the harmonics data for 637 US stations.  The harmonics data
    was converted from
    <https://github.com/poissonconsulting/rtide/blob/master/data-raw/harmonics-dwf-20151227-free.tar.bz2>,
    NOAA web site data processed by David Flater for 'XTide'.  The code to
    calculate tide heights from the harmonics is based on 'XTide'.
	"""
	
	homepage = "https://github.com/poissonconsulting/rtide"
	cran = "rtide" 

	version("0.0.9", md5="9c5dccf180af39fda0da1569c21fd0c5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-dttr2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
