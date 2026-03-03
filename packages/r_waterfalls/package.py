# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaterfalls(RPackage):
	"""Create Waterfall Charts using 'ggplot2' Simply

	A not uncommon task for quants is to create 'waterfall charts'. There seems to be no simple way to do this in 'ggplot2' currently. This package contains a single function (waterfall) that simply draws a waterfall chart in a 'ggplot2' object. Some flexibility is provided, though often the object created will need to be modified through a theme.
	"""
	
	homepage = "https://github.com/hughparsonage/waterfalls"
	cran = "waterfalls" 

	version("1.0.0", md5="5321be9186d29cab12321cc1f3ca3ecf")

	depends_on("r-ggplot2@2:", type=("build", "run"))
