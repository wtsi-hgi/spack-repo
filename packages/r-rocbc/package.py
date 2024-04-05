# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocbc(RPackage):
	"""Statistical Inference for Box-Cox Based Receiver Operating
Characteristic Curves

	Generation of Box-Cox based ROC curves and several aspects of inferences and hypothesis testing. Can be used when inferences for one biomarker (Bantis LE, Nakas CT, Reiser B. (2018) <doi:10.1002/bimj.201700107>) are of interest or when comparisons of two correlated biomarkers (Bantis LE, Nakas CT, Reiser B. (2021) <doi:10.1002/bimj.202000128>) are of interest. Provides inferences and comparisons around the AUC, the Youden index, the sensitivity at a given specificity level (and vice versa), the optimal operating point of the ROC curve (in the Youden sense), and the Youden based cutoff.
	"""
	
	cran = "rocbc" 

	version("3.0.0", md5="c88e5d48ee5006b6f8aac7978bf6601b")
	version("2.0.0", md5="acd716b414a613ce9bbc39fb1c4947df")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-clinfun", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-mrmcaov", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
