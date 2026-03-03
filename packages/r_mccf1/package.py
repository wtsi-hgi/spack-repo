# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMccf1(RPackage):
	"""Creates the MCC-F1 Curve and Calculates the MCC-F1 Metric and
the Best Threshold

	The MCC-F1 analysis is a method to evaluate the performance of binary classifications. 
    The MCC-F1 curve is more reliable than the Receiver Operating Characteristic (ROC) curve and the Precision-Recall (PR)curve under imbalanced ground truth.
    The MCC-F1 analysis also provides the MCC-F1 metric that integrates classifier performance over varying thresholds, and the best threshold of binary classification.
	"""
	
	homepage = "https://bitbucket.org/hoffmanlab/mccf1/"
	cran = "mccf1" 

	version("1.1", md5="2d92597d0c4522a88ec61394e03ecc97", url="https://cran.r-project.org/src/contrib/mccf1_1.1.tar.gz")

	depends_on("r@3.3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
