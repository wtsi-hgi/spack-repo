# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGemma2(RPackage):
	"""GEMMA Multivariate Linear Mixed Model

	Fits a multivariate linear mixed effects model that uses a polygenic term, after Zhou & Stephens (2014) (<https://www.nature.com/articles/nmeth.2848>). Of particular interest is the estimation of variance components with restricted maximum likelihood (REML) methods. Genome-wide efficient mixed-model association (GEMMA), as implemented in the package 'gemma2', uses an expectation-maximization algorithm for variance components inference for use in quantitative trait locus studies.
	"""
	
	homepage = "https://github.com/fboehm/gemma2"
	cran = "gemma2" 

	version("0.1.3", md5="f13f8117031ce5c3420302a473f8d5f8", url="https://cran.r-project.org/src/contrib/gemma2_0.1.3.tar.gz")

	depends_on("r-matrix", type=("build", "run"))
