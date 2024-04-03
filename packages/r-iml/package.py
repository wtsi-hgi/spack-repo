# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIml(RPackage):
	"""Interpretable Machine Learning

	Interpretability methods to analyze the behavior and
    predictions of any machine learning model.  Implemented methods are:
    Feature importance described by Fisher et al. (2018)
    <arXiv:1801.01489>, accumulated local effects plots described by Apley
    (2018) <arXiv:1612.08468>, partial dependence plots described by
    Friedman (2001) <www.jstor.org/stable/2699986>, individual conditional
    expectation ('ice') plots described by Goldstein et al.  (2013)
    <doi:10.1080/10618600.2014.907095>, local models (variant of 'lime')
    described by Ribeiro et. al (2016) <arXiv:1602.04938>, the Shapley
    Value described by Strumbelj et. al (2014)
    <doi:10.1007/s10115-013-0679-x>, feature interactions described by
    Friedman et. al <doi:10.1214/07-AOAS148> and tree surrogate models.
	"""
	
	homepage = "https://christophm.github.io/iml/"
	cran = "iml" 

	version("0.11.2", md5="64de95cfe6930b47f43228d7712af662")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
