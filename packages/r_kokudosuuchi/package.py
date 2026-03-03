# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKokudosuuchi(RPackage):
	"""Utilities for 'Kokudo Suuchi'

	Provides utilities for 'Kokudo Suuchi', the GIS data service of the Japanese government.
    See <https://nlftp.mlit.go.jp/index.html> for more information.
	"""
	
	homepage = "https://yutannihilation.github.io/kokudosuuchi/"
	cran = "kokudosuuchi" 

	version("1.0.0", md5="36323eeb007a765a811ee26ceff6a915")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
