# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExcel2eprime(RPackage):
	"""Split Sentences by Factors

	Split experiment sentences by different experiment design given by the user and the result can be used in 'E-prime' (<https://pstnet.com/products/e-prime/>).
	"""
	
	homepage = "https://github.com/wujackwill/excel2eprime"
	cran = "excel2eprime" 

	version("0.4.0", md5="9fe92e2e65e1b36f3ad0da2a543f0a3f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
