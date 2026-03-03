# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPawacc(RPackage):
	"""Physical Activity with Accelerometers

	Functions to process, format and store ActiGraph GT1M and GT3X accelerometer data.
	"""
	
	cran = "pawacc" 

	version("1.2.3", md5="18f1abf092f07584ea1e3f7f2724f549")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
