# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMxm(RPackage):
	"""Feature Selection (Including Multiple Solutions) and Bayesian
Networks

	Many feature selection methods for a wide range of response variables, including minimal, statistically-equivalent and equally-predictive feature subsets. Bayesian network algorithms and related functions are also included. The package name 'MXM' stands for "Mens eX Machina", meaning "Mind from the Machine" in Latin. References: a) Lagani, V. and Athineou, G. and Farcomeni, A. and Tsagris, M. and Tsamardinos, I. (2017). Feature Selection with the R Package MXM: Discovering Statistically Equivalent Feature Subsets. Journal of Statistical Software, 80(7). <doi:10.18637/jss.v080.i07>. b) Tsagris, M., Lagani, V. and Tsamardinos, I. (2018). Feature selection for high-dimensional temporal data. BMC Bioinformatics, 19:17. <doi:10.1186/s12859-018-2023-7>. c) Tsagris, M., Borboudakis, G., Lagani, V. and Tsamardinos, I. (2018). Constraint-based causal discovery with mixed data. International Journal of Data Science and Analytics, 6(1): 19-30. <doi:10.1007/s41060-018-0097-y>. d) Tsagris, M., Papadovasilakis, Z., Lakiotaki, K. and Tsamardinos, I. (2018). Efficient feature selection on gene expression data: Which algorithm to use? BioRxiv. <doi:10.1101/431734>. e) Tsagris, M. (2019). Bayesian Network Learning with the PC Algorithm: An Improved and Correct Variation. Applied Artificial Intelligence, 33(2):101-123. <doi:10.1080/08839514.2018.1526760>. f) Tsagris, M. and Tsamardinos, I. (2019). Feature selection with the R package MXM. F1000Research 7: 1505. <doi:10.12688/f1000research.16216.2>. g) Borboudakis, G. and Tsamardinos, I. (2019). Forward-Backward Selection with Early Dropping. Journal of Machine Learning Research 20: 1-39. h) The gamma-OMP algorithm for feature selection with application to gene expression data. IEEE/ACM Transactions on Computational Biology and Bioinformatics 19(2): 1214-1224. <doi:10.1109/TCBB.2020.3029952>.
	"""
	
	homepage = "http://mensxmachina.org"
	cran = "MXM" 

	version("1.5.5", md5="82a46b8ade7c9ca7e213e3ffee075000")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-relations", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-rfast2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
