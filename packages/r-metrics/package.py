# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetrics(RPackage):
	"""Evaluation Metrics for Machine Learning

	An implementation of evaluation metrics in R that are commonly
             used in supervised machine learning. It implements metrics for
             regression, time series, binary classification, classification,
             and information retrieval problems. It has zero dependencies and
             a consistent, simple interface for all functions.
	"""
	
	homepage = "https://github.com/mfrasco/Metrics"
	cran = "Metrics" 

	version("0.1.4", md5="b2202269b66cd891b834d742cfd937ba")

