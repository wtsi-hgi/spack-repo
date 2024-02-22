# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpdo(RPackage):
	"""Pacific Decadal Oscillation Index Data

	Monthly Pacific Decadal Oscillation (PDO) index values from
    January 1900 to September 2018.  Superseded by 'rsoi' package which
    includes the historical and most recent monthly PDO index values
    together with related climate indices.
	"""
	
	homepage = "https://github.com/poissonconsulting/rpdo"
	cran = "rpdo" 

	version("0.3.2", md5="0301301f4555da79097e64d724de42c2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
