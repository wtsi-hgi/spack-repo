# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPivotea(RPackage):
	"""Create Pivot Table Easily

	Pivot easily by specifying rows, columns, values and split.
	"""
	
	homepage = "https://github.com/matutosi/pivotea"
	cran = "pivotea" 

	version("1.0.1", md5="e33c6255ced45b43af4b195ccd63b3d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
