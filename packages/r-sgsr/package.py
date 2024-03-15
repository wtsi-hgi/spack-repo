# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgsr(RPackage):
	"""Structurally Guided Sampling

	Structurally guided sampling (SGS) approaches for airborne laser scanning (ALS; LIDAR). Primary functions provide means 
    to generate data-driven stratifications & methods for allocating samples. Intermediate functions for calculating and extracting important information 
    about input covariates and samples are also included. Processing outcomes are intended to help forest and environmental management
    practitioners better optimize field sample placement as well as assess and augment existing sample networks in the context of data
    distributions and conditions. ALS data is the primary intended use case, however any rasterized remote sensing data can be used, 
    enabling data-driven stratifications and sampling approaches.
	"""
	
	homepage = "https://github.com/tgoodbody/sgsR"
	cran = "sgsR" 

	version("1.4.5", md5="8c7ad544592dbd2ce48319caa2744782")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-clhs", type=("build", "run"))
	depends_on("r-samplingbigdata", type=("build", "run"))
	depends_on("r-balancedsampling", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
