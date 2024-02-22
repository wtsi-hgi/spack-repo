# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfishnet2(RPackage):
	"""Exploratory Data Analysis for FishNet2 Data

	Provides data processing and summarization of data from FishNet2.net
  in text and graphical outputs. Allows efficient filtering of information and
  data cleaning.
	"""
	
	homepage = "https://github.com/kdors/rfishnet2"
	cran = "rfishnet2" 

	version("0.2.0", md5="6fa8e96f38ccb6488eecc3ff498bb0f5", url="https://cran.r-project.org/src/contrib/rfishnet2_0.2.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-pracma@2.2.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-sf@0.8.0:", type=("build", "run"))
	depends_on("r-rworldmap@1.3.6:", type=("build", "run"))
