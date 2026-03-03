# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStray(RPackage):
	"""Anomaly Detection in High Dimensional and Temporal Data

	
    This is a modification of 'HDoutliers' package. The 'HDoutliers' algorithm is a powerful 
    unsupervised algorithm for detecting anomalies in high-dimensional data, with a 
    strong theoretical foundation. However, it suffers from some limitations that 
    significantly hinder its performance level, under certain circumstances. This package 
    implements the algorithm proposed in Talagala, Hyndman and Smith-Miles (2019) 
    <arXiv:1908.04000>  for detecting anomalies in high-dimensional data
    that addresses these limitations of 'HDoutliers' algorithm. We define an anomaly as an observation that deviates markedly from the majority
    with a large distance gap. An approach based on extreme value theory is used 
    for the anomalous threshold calculation.
	"""
	
	cran = "stray" 

	version("0.1.1", md5="35d2e53d8e28e2b0c0c1a76a61ee5d46")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
