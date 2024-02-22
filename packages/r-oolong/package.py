# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROolong(RPackage):
	"""Create Validation Tests for Automated Content Analysis

	Intended to create standard human-in-the-loop validity tests for typical automated content analysis such as topic modeling and dictionary-based methods. This package offers a standard workflow with functions to prepare, administer and evaluate a human-in-the-loop validity test. This package provides functions for validating topic models using word intrusion, topic intrusion (Chang et al. 2009,  <https://papers.nips.cc/paper/3700-reading-tea-leaves-how-humans-interpret-topic-models>) and word set intrusion (Ying et al. 2021) <doi:10.1017/pan.2021.33> tests. This package also provides functions for generating gold-standard data which are useful for validating dictionary-based methods. The default settings of all generated tests match those suggested in Chang et al. (2009) and Song et al. (2020) <doi:10.1080/10584609.2020.1723752>.
	"""
	
	homepage = "https://gesistsa.github.io/oolong/"
	cran = "oolong" 

	version("0.6.0", md5="043154867da724f7be1a6e7fc9d498f0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-seededlda", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-quanteda@3:", type=("build", "run"))
	depends_on("r-irr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
