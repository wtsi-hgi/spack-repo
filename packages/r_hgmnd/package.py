# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgmnd(RPackage):
	"""Heterogeneous Graphical Model for Non-Negative Data

	Graphical model is an informative and powerful tool to explore the conditional dependence relationships among variables. The traditional Gaussian graphical model and its extensions either have a Gaussian assumption on the data distribution or assume the data are homogeneous. However, there are data with complex distributions violating these two assumptions. For example, the air pollutant concentration records are non-negative and, hence, non-Gaussian. Moreover, due to climate changes, distributions of these concentration records in different months of a year can be far different, which means it is uncertain whether datasets from different months are homogeneous. Methods with a Gaussian or homogeneous assumption may incorrectly model the conditional dependence relationships among variables. Therefore, we propose a heterogeneous graphical model for non-negative data (HGMND) to simultaneously cluster multiple datasets and estimate the conditional dependence matrix of variables from a non-Gaussian and non-negative exponential family in each cluster.
	"""
	
	cran = "HGMND" 

	version("0.1.0", md5="efda5d6b5b5314800c4c2336621b41cd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-genscore", type=("build", "run"))
