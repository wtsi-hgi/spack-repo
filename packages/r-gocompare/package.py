# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGocompare(RPackage):
	"""Comprehensive GO Terms Comparison Between Species

	Supports the assessment of functional enrichment analyses obtained for several lists of genes and provides a workflow to analyze them between two species via weighted graphs. Methods are described in Sosa et al. (2023) <doi:10.1016/j.ygeno.2022.110528>.
	"""
	
	homepage = "https://github.com/ccsosa/GOCompare"
	cran = "GOCompare" 

	version("1.0.2.1", md5="a51d71498c3a7d9a89cf0356c89f115b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
