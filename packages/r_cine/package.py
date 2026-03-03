# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCine(RPackage):
	"""Classification International Normalized of Education

	Function using lemmatization to classify educational programs according to the CINE(Classification International Normalized of Education) for Peru.
	"""
	
	homepage = "https://github.com/musajajorge/CINE"
	cran = "CINE" 

	version("0.1.3", md5="a60cc4c2e242f0d40272bc6347bc4716")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
