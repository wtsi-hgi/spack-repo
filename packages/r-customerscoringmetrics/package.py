# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomerscoringmetrics(RPackage):
	"""Evaluation Metrics for Customer Scoring Models Depending on
Binary Classifiers

	Functions for evaluating and visualizing predictive model performance (specifically: binary classifiers) in the field of customer scoring. These metrics include lift, lift index, gain percentage, top-decile lift, F1-score, expected misclassification cost and absolute misclassification cost. See Berry & Linoff (2004, ISBN:0-471-47064-3), Witten and Frank (2005, 0-12-088407-0) and Blattberg, Kim & Neslin (2008, ISBN:978–0–387–72578–9) for details. Visualization functions are included for lift charts and gain percentage charts. All metrics that require class predictions offer the possibility to dynamically determine cutoff values for transforming real-valued probability predictions into class predictions.
	"""
	
	cran = "CustomerScoringMetrics" 

	version("1.0.0", md5="20f05ce33402f0f97efb4c46e6b89704")

