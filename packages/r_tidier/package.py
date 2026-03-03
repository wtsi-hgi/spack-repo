# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidier(RPackage):
	"""Enhanced 'mutate'

	Provides 'Apache Spark' style window aggregation for R dataframes and remote 'dbplyr' tables via 'mutate' in 'dplyr' flavour.
	"""
	
	homepage = "https://github.com/talegari/tidier"
	cran = "tidier" 

	version("0.2.0", md5="ce146b0a587f10d92fd9ff46bb404329")

	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-slider@0.2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-furrr@0.3:", type=("build", "run"))
	depends_on("r-dbplyr@2.3.1:", type=("build", "run"))
