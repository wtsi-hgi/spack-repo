# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaxentvariableselection(RPackage):
	"""Selecting the Best Set of Relevant Environmental Variables along
with the Optimal Regularization Multiplier for Maxent Niche
Modeling

	Complex niche models show low performance in identifying
    the most important range-limiting environmental variables and in
    transferring habitat suitability to novel environmental conditions
    (Warren and Seifert, 2011 <DOI:10.1890/10-1171.1>; Warren et al.,
    2014 <DOI:10.1111/ddi.12160>). This package helps to identify the
    most important set of uncorrelated variables and to fine-tune Maxent's
    regularization multiplier. In combination, this allows to constrain
    complexity and increase performance of Maxent niche models (assessed
    by information criteria, such as AICc (Akaike, 1974
    <DOI:10.1109/TAC.1974.1100705>), and by the area under the receiver
    operating characteristic (AUC) (Fielding and Bell, 1997
    <DOI:10.1017/S0376892997000088>). Users of this package should be
    familiar with Maxent niche modelling.
	"""
	
	cran = "MaxentVariableSelection" 

	version("1.0-3", md5="63976c0edaf9ff232b8937617303bce7")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
