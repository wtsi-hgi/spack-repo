# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrobblr(RPackage):
	"""Creating Flexible, Reproducible 'PDF' Reports

	A tool which allows users the ability to intuitively create 
  flexible, reproducible portable document format reports comprised of 
  aesthetically pleasing tables, images, plots and/or text.
	"""
	
	cran = "grobblR" 

	version("0.2.1", md5="8757bc11350ef952c53ae9d57753d1e3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
