# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecometrics(RPackage):
	"""Evaluation Metrics for Implicit-Feedback Recommender Systems

	Calculates evaluation metrics for implicit-feedback recommender systems
  that are based on low-rank matrix factorization models, given the fitted model
  matrices and data, thus allowing to compare models from a variety of libraries.
  Metrics include P@K (precision-at-k, for top-K recommendations), R@K (recall at k),
  AP@K (average precision at k), NDCG@K (normalized discounted cumulative gain at k),
  Hit@K (from which the 'Hit Rate' is calculated), RR@K (reciprocal rank at k, from
  which the 'MRR' or 'mean reciprocal rank' is calculated), ROC-AUC (area under the
  receiver-operating characteristic curve), and PR-AUC (area under the
  precision-recall curve).
  These are calculated on a per-user basis according to the ranking of items induced
  by the model, using efficient multi-threaded routines. Also provides functions
  for creating train-test splits for model fitting and evaluation.
	"""
	
	homepage = "https://github.com/david-cortes/recometrics"
	cran = "recometrics" 

	version("0.1.6-3", md5="999b64cabdefa4f4f76e14da408d3e12")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.3.4:", type=("build", "run"))
	depends_on("r-matrixextra@0.1.6:", type=("build", "run"))
	depends_on("r-float", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
