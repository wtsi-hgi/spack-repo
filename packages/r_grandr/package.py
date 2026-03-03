# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrandr(RPackage):
	"""Comprehensive Analysis of Nucleotide Conversion Sequencing Data

	Nucleotide conversion sequencing experiments have been
  developed to add a temporal dimension to RNA-seq and single-cell RNA-seq. Such 
  experiments require specialized tools for primary processing such as GRAND-SLAM,
  (see 'Jürges et al' <doi:10.1093/bioinformatics/bty256>) and specialized tools for 
  downstream analyses. 'grandR' provides a comprehensive toolbox for quality control,
  kinetic modeling, differential gene expression analysis and visualization of such data.
	"""
	
	homepage = "https://github.com/erhard-lab/grandR"
	cran = "grandR" 

	version("0.2.5", md5="355e6dc5620e9884dce6c6ac2460397a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-lfc", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
