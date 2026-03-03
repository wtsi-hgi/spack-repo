# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfilt(RPackage):
	"""Collaborative Filtering by Reference Classes

	The collaborative Filtering methodology has been widely used in recommendation systems, which
    uses similarities between users or items to make recommendations. A class called CF was implemented,
    where it is structured by matrices and composed of recommendation and database manipulation functions.
    See Aggarwal (2016) <doi:10.1007/978-3-319-29659-3> for an overview. 
	"""
	
	cran = "CFilt" 

	version("0.2.1", md5="eb59a81b13aaebfa3720330dca950b74")

	depends_on("r@3.5:", type=("build", "run"))
