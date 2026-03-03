# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RText2sdg(RPackage):
	"""Detecting UN Sustainable Development Goals in Text

	The United Nations’ Sustainable Development Goals (SDGs) have become an important guideline for organisations to monitor and plan their contributions to social, economic, and environmental transformations. The 'text2sdg' package is an open-source analysis package that identifies SDGs in text using scientifically developed query systems, opening up the opportunity to monitor any type of text-based data, such as scientific output or corporate publications. For more information regarding the methodology see Meier, Mata & Wulff (2022) <arXiv:2110.05856>.
	"""
	
	homepage = "https://github.com/dwulff/text2sdg"
	cran = "text2sdg" 

	version("1.1.1", md5="d8d4a8bf3d0c33f94cd861a3f4dfb9b0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-corpustools@0.4.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-text2sdgdata@0.1.1:", type=("build", "run"))
