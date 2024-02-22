# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrequency(RPackage):
	"""Easy Frequency Tables

	Generate 'SPSS'/'SAS' styled frequency tables. Frequency tables are 
    generated with variable and value label attributes where applicable with optional
    html output to quickly examine datasets.
	"""
	
	homepage = "https://github.com/wilcoxa/frequency"
	cran = "frequency" 

	version("0.4.1", md5="3022c2b8b22f4d5d7e585e9d8be1479c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
