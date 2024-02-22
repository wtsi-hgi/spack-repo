# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolitude(RPackage):
	"""An Implementation of Isolation Forest

	Isolation forest is anomaly detection method introduced by the paper Isolation based Anomaly Detection (Liu, Ting and Zhou <doi:10.1145/2133360.2133363>).
	"""
	
	homepage = "https://github.com/talegari/solitude"
	cran = "solitude" 

	version("1.1.3", md5="4cb491e13d3b010d7207d2c6b04572eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ranger@0.11:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-igraph@1.2.2:", type=("build", "run"))
	depends_on("r-future-apply@0.2:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-lgr@0.3.4:", type=("build", "run"))
