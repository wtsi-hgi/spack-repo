# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnanseseurat(RPackage):
	"""Construct ANANSE GRN-Analysis Seurat

	Enables gene regulatory network (GRN) analysis on single cell clusters,
    using the GRN analysis software 'ANANSE', Xu et al.(2021) <doi:10.1093/nar/gkab598>.
    Export data from 'Seurat' objects, for GRN analysis by 'ANANSE' 
    implemented in 'snakemake'. Finally, incorporate results for visualization 
    and interpretation.
	"""
	
	homepage = "https://github.com/JGASmits/AnanseSeurat/"
	cran = "AnanseSeurat" 

	version("1.2.0", md5="dfd9db6a092ba288b1b252da3e0bfbae")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
