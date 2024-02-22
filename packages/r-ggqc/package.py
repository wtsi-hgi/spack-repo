# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgqc(RPackage):
	"""Quality Control Charts for 'ggplot'

	Plot single and faceted type quality control charts
  for 'ggplot'.  
	"""
	
	cran = "ggQC" 

	version("0.0.31", md5="8a2165f44850dcd8481e5faefc28a577")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
