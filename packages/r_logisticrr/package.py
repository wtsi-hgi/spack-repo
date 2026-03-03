# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogisticrr(RPackage):
	"""Adjusted Relative Risk from Logistic Regression

	Adjusted odds ratio conditional on potential confounders can be directly obtained from logistic regression. However, those adjusted odds ratios have been widely incorrectly interpreted as a relative risk. As relative risk is often of interest in public health, we provide a simple code to return adjusted relative risks from logistic regression model under potential confounders. 
	"""
	
	homepage = "https://github.com/youjin1207/logisticRR"
	cran = "logisticRR" 

	version("0.3.0", md5="c510ba8753dc6c6f1536a448a9a5c63f")

	depends_on("r-nnet", type=("build", "run"))
