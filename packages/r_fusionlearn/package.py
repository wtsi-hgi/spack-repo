# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusionlearn(RPackage):
	"""Fusion Learning

	The fusion learning method uses a model selection algorithm to learn from multiple data sets across different experimental platforms through group penalization. The responses of interest may include a mix of discrete and continuous variables. The responses may share the same set of predictors, however, the models and parameters differ across different platforms. Integrating information from different data sets can enhance the power of model selection. Package is based on Xin Gao, Raymond J. Carroll (2017) <arXiv:1610.00667v1>. 
	"""
	
	cran = "FusionLearn" 

	version("0.2.1", md5="6e623ed4543b6b85b2f88986f492d980")

	depends_on("r@3.5:", type=("build", "run"))
