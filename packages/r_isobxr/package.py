# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsobxr(RPackage):
	"""Stable Isotope Box Modelling in R

	A set of functions to run simple and composite box-models to describe the 
    dynamic or static distribution of stable isotopes in open 
    or closed systems. The package also allows the sweeping of many 
    parameters in both static and dynamic conditions.
    The mathematical models used in this package are derived from Albarede, 1995, 
    Introduction to Geochemical Modelling, Cambridge University Press,
    Cambridge <doi:10.1017/CBO9780511622960>.
	"""
	
	homepage = "https://github.com/ttacail/isobxr"
	cran = "isobxr" 

	version("2.0.0", md5="221254bce03b9c2ce5cba7472c7fb31b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
