# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzplot(RPackage):
	"""Functions for Common Chart Types

	Wrapper for the 'ggplot2' package that creates a variety of common
  charts (e.g. bar, line, area, ROC, waterfall, pie) while aiming to reduce
  typing. 
	"""
	
	cran = "ezplot" 

	version("0.7.13", md5="2338896d4fdabe1897b277e6b15f3c9d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
