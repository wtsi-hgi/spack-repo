# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVia(RPackage):
	"""Virtual Arrays

	The base class 'VirtualArray' is defined, which acts as a wrapper around lists allowing users to fold arbitrary sequential data into n-dimensional, R-style virtual arrays. The derived 'XArray' class is defined to be used for homogeneous lists that contain a single class of objects. The 'RasterArray' and 'SfArray' classes enable the use of stacked spatial data instead of lists.
	"""
	
	cran = "via" 

	version("0.2.0", md5="486960b250a37c16bee9655b0bc77b3f")

	depends_on("r@4:", type=("build", "run"))
