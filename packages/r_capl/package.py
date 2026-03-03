# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCapl(RPackage):
	"""Compute and Visualize CAPL-2 Scores and Interpretations

	A toolkit for computing and visualizing CAPL-2
    (Canadian Assessment of Physical Literacy, Second Edition;
    <https://www.capl-eclp.ca>) scores and interpretations from raw data.
	"""
	
	homepage = "https://github.com/barnzilla/capl"
	cran = "capl" 

	version("1.42", md5="93ef444032f18eb9ed9df59633788eb8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
