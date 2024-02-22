# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWarp(RPackage):
	"""Group Dates

	Tooling to group dates by a variety of periods including:
    yearly, monthly, by second, by week of the month, and more.  The
    groups are defined in such a way that they also represent the distance
    between dates in terms of the period. This extracts valuable
    information that can be used in further calculations that rely on a
    specific temporal spacing between observations.
	"""
	
	homepage = "https://github.com/DavisVaughan/warp"
	cran = "warp" 

	version("0.2.1", md5="0e3d587557c124f3ffa93118677f962d")

	depends_on("r@3.2:", type=("build", "run"))
