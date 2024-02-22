# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaaccr(RPackage):
	"""Read Cancer Records in the NAACCR Format

	Functions for reading cancer record files which follow a format
    defined by the North American Association of Central Cancer Registries
    (NAACCR).
	"""
	
	homepage = "https://github.com/WerthPADOH/naaccr"
	cran = "naaccr" 

	version("2.0.2", md5="c549f9cc2080b182f5589a58cd31a8f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
