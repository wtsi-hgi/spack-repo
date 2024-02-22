# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemospecutils(RPackage):
	"""Functions Supporting Packages ChemoSpec and ChemoSpec2D

	Functions supporting the common needs of packages 'ChemoSpec' and 'ChemoSpec2D'.
	"""
	
	homepage = "https://github.com/bryanhanson/ChemoSpecUtils"
	cran = "ChemoSpecUtils" 

	version("1.0.4", md5="60c49ef5a4206ffeadef817a83f7e62e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
