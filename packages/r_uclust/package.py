# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUclust(RPackage):
	"""Clustering and Classification Inference with U-Statistics

	Clustering and classification inference for high dimension low sample size (HDLSS)
    data with U-statistics. The package contains implementations of nonparametric statistical
    tests for sample homogeneity, group separation, clustering, and classification of 
    multivariate data. The methods have high statistical power and are tailored for data
    in which the dimension L is much larger than sample size n. See Gabriela B. Cybis,
    Marcio Valk and Sílvia RC Lopes (2018) <doi:10.1080/00949655.2017.1374387>, Marcio 
    Valk and Gabriela B. Cybis (2020) <doi:10.1080/10618600.2020.1796398>, Debora Z. Bello, Marcio 
    Valk and Gabriela B. Cybis (2021) <arXiv:2106.09115>. 
	"""
	
	cran = "uclust" 

	version("1.0.0", md5="3e7399cd19c1f92e75e492d4719d966f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-robcor", type=("build", "run"))
