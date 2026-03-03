# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidylog(RPackage):
	"""Logging for 'dplyr' and 'tidyr' Functions

	Provides feedback about 'dplyr' and 'tidyr' operations.
	"""
	
	homepage = "https://github.com/elbersb/tidylog/"
	cran = "tidylog" 

	version("1.0.2", md5="17c4e3a5589ac9a1a0653ba54e979d52")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-clisymbols", type=("build", "run"))
