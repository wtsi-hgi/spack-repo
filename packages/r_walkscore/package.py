# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalkscore(RPackage):
	"""A Tidy Interface to the 'Walk Score' API

	Easily collect walk scores, bike scores, and transit scores (where
    available) from the 'Walk Score' API <https://www.walkscore.com/professional/api.php>, 
    a proprietary API that assigns locations a walkability score between 0 and 100.
	"""
	
	homepage = "https://github.com/chris31415926535/walkscore"
	cran = "walkscore" 

	version("0.1.2", md5="cd367c045be3fab5d4df9cc483548fcc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
