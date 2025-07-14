# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructtoolbox(RPackage):
	"""Data processing & analysis tools for Metabolomics and other omics

	An extensive set of data (pre-)processing and analysis methods and tools for metabolomics and other omics, with a strong emphasis on statistics and machine learning. This toolbox allows the user to build extensive and standardised workflows for data analysis. The methods and tools have been implemented using class-based templates provided by the struct (Statistics in R Using Class-based Templates) package. The toolbox includes pre-processing methods (e.g. signal drift and batch correction, normalisation, missing value imputation and scaling), univariate (e.g. ttest, various forms of ANOVA, Kruskal–Wallis test and more) and multivariate statistical methods (e.g. PCA and PLS, including cross-validation and permutation testing) as well as machine learning methods (e.g. Support Vector Machines). The STATistics Ontology (STATO) has been integrated and implemented to provide standardised definitions for the different methods, inputs and outputs.
	"""
	
	homepage = "https://github.com/computational-metabolomics/structToolbox"
	bioc = "structToolbox"

	version("1.20.0", commit="166843836d3ec6af93a2ad473638acb9e221c277")
	version("1.14.0", commit="f3b802f403417bdd60ab274de12380385c138345")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-struct@1.5.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
