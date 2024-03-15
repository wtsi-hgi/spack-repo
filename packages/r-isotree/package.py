# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsotree(RPackage):
	"""Isolation-Based Outlier Detection

	Fast and multi-threaded implementation of
	isolation forest (Liu, Ting, Zhou (2008) <doi:10.1109/ICDM.2008.17>),
	extended isolation forest (Hariri, Kind, Brunner (2018) <arXiv:1811.02141>),
	SCiForest (Liu, Ting, Zhou (2010) <doi:10.1007/978-3-642-15883-4_18>),
	fair-cut forest (Cortes (2021) <arXiv:2110:13402>),
	robust random-cut forest (Guha, Mishra, Roy, Schrijvers (2016) <http://proceedings.mlr.press/v48/guha16.html>),
	and customizable variations of them, for isolation-based outlier detection, clustered outlier detection,
	distance or similarity approximation (Cortes (2019) <arXiv:1910.12362>),
	isolation kernel calculation (Ting, Zhu, Zhou (2018) <doi:10.1145/3219819.3219990>),
	and imputation of missing values (Cortes (2019) <arXiv:1911.06646>),
	based on random or guided decision tree splitting, and providing different metrics for
	scoring anomalies based on isolation depth or density (Cortes (2021) <arXiv:2111.11639>).
	Provides simple heuristics for fitting the model to categorical columns and handling missing data,
	and offers options for varying between random and guided splits, and for using different splitting criteria.
	"""
	
	homepage = "https://github.com/david-cortes/isotree"
	cran = "isotree" 

	version("0.5.24-3", md5="187c07e96a3e58931b39747e3aa18112")

	depends_on("r-rcpp", type=("build", "run"))
