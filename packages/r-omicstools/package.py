# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicstools(RPackage):
	"""Omics Data Process Toolbox

	Processing and analyzing omics data from genomics, transcriptomics, proteomics, and metabolomics platforms. It provides functions for preprocessing, normalization, visualization, and statistical analysis, as well as machine learning algorithms for predictive modeling. 'omicsTools' is an essential tool for researchers working with high-throughput omics data in fields such as biology, bioinformatics, and medicine.The QC-RLSC (quality control–based robust LOESS signal correction) algorithm is used for normalization. Dunn et al. (2011) <doi:10.1038/nprot.2011.335>.
	"""
	
	homepage = "https://github.com/YaoxiangLi/omicsTools"
	cran = "omicsTools" 

	version("1.0.5", md5="31acd9ddea33268f35c46ee6c66ea1cf")

	depends_on("r-bs4dash", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-shiny@1.7.2:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
