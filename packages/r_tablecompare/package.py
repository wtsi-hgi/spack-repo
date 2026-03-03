# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTablecompare(RPackage):
	"""Compare Data Frames

	A toolbox for comparing two data frames. This package is defunct. I recommend you use the "versus" package instead.
	"""
	
	homepage = "https://github.com/eutwt/tablecompare"
	cran = "tablecompare" 

	version("0.1.1", md5="65caecc8ba4229a2c1aea0e8ff768625")

	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.3:", type=("build", "run"))
	depends_on("r-tidyselect@0.4.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
