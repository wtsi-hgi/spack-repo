# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvaluationmeasures(RPackage):
	"""Collection of Model Evaluation Measure Functions

	Provides Some of the most important evaluation measures for evaluating a model. Just by giving the real and predicted class, measures such as accuracy, sensitivity, specificity, ppv, npv, fmeasure, mcc and ... will be returned.
	"""
	
	cran = "EvaluationMeasures" 

	version("1.1.0", md5="3502b699c88979e4ef410b36788821d1")

