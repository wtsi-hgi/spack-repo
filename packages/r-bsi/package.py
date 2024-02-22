# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsi(RPackage):
	"""Modeling and Computing Biogenic Silica ('bSi') from Inland and
Pelagic Sediments

	A collection of integrated tools designed to seamlessly interact with each other for the analysis of biogenic silica 'bSi' in inland and marine sediments. These tools share common data representations and follow a consistent 'API' design. The primary goal of the 'bSi' package is to simplify the installation process, facilitate data loading, and enable the analysis of multiple samples for biogenic silica fluxes. This package is designed to enhance the efficiency and coherence of the entire 'bSi' analytic workflow, from data loading to model construction and visualization tailored towards reconstructing productivity in aquatic ecosystems.
	"""
	
	cran = "bSi" 

	version("1.0.0", md5="963b5d8648a58bec19aa5a0200f890c9")

	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
