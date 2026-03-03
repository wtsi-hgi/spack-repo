# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyfast(RPackage):
	"""Fast Tidying of Data

	Tidying functions built on 'data.table'
    to provide quick and efficient data manipulation with
    minimal overhead.
	"""
	
	cran = "tidyfast" 

	version("0.4.0", md5="cbbe023bc1d6216c8ad2d3ac1cdab549")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table@1.13.4:", type=("build", "run"))
	depends_on("r-cpp11@0.2.6:", type=("build", "run"))
