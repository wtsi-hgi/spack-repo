# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiom2(RPackage):
	"""Biologically Explainable Machine Learning Framework

	Biologically Explainable Machine Learning Framework for Phenotype Prediction using omics data described in Chen and Schwarz (2017) <arXiv:1712.0036v1>.Identifying reproducible and interpretable biological patterns from high-dimensional omics data is a critical factor in understanding the risk mechanism of complex disease. As such, explainable machine learning can offer biological insight in addition to personalized risk scoring.In this process, a feature space of biological pathways will be generated, and the feature space can also be subsequently analyzed using WGCNA (Described in Horvath and Zhang (2005) <doi:10.2202/1544-6115.1128> and Langfelder and Horvath (2008) <doi:10.1186/1471-2105-9-559> ) methods.
	"""
	
	cran = "BioM2" 

	version("1.0.3", md5="a50204f41d7abb83c7ec67f9a2fe4062", url="https://cran.r-project.org/src/contrib/BioM2_1.0.3.tar.gz")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-cmplot", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-ggstatsplot", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jiebar", type=("build", "run"))
	depends_on("r-mlr3verse", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-webshot", type=("build", "run"))
	depends_on("r-wordcloud2", type=("build", "run"))
	depends_on("r-intergraph", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggnetwork", type=("build", "run"))
