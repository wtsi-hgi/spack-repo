# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPriceindices(RPackage):
	"""Calculating Bilateral and Multilateral Price Indexes

	Preparing a scanner data set for price dynamics calculations (data selecting, data classification, data matching, data filtering). Computing bilateral and multilateral indexes. For details on these methods see: Diewert and Fox (2020) 
    <doi:10.1080/07350015.2020.1816176>, Białek (2019) <doi:10.2478/jos-2019-0014> or Białek (2020) <doi:10.2478/jos-2020-0037>.
	"""
	
	cran = "PriceIndices" 

	version("0.1.8", md5="54883c04933dba292af646da16e86c58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-reclin2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-strex", type=("build", "run"))
