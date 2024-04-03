# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScdeconr(RPackage):
	"""Deconvolution of Bulk RNA-Seq Data using Single-Cell RNA-Seq
Data as Reference

	Streamlined workflow from deconvolution of bulk RNA-seq data to downstream differential expression and gene-set enrichment analysis. Provide various visualization functions. 
	"""
	
	homepage = "https://github.com/Liuy12/SCdeconR/"
	cran = "SCdeconR" 

	version("1.0.0", md5="647b3e31bc73574df506f029bf1a34b3")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-glmgampoi", type=("build", "run"))
