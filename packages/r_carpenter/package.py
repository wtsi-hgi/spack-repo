# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarpenter(RPackage):
	"""Build Common Tables of Summary Statistics for Reports

	Mainly used to build tables that are commonly presented for
    bio-medical/health research, such as basic characteristic tables or
    descriptive statistics.
	"""
	
	homepage = "https://github.com/lwjohnst86/carpenter"
	cran = "carpenter" 

	version("0.2.2", md5="e5cac33df60c7b768164eaa5daded1a4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
