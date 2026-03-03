# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLcaextend(RPackage):
	"""Latent Class Analysis (LCA) with Familial Dependence in Extended
Pedigrees

	Latent Class Analysis of
        phenotypic measurements in pedigrees and model selection
        based on one of two methods: likelihood-based cross-validation
        and Bayesian Information Criterion. Computation of individual
        and triplet child-parents weights in a pedigree is performed using an
        upward-downward algorithm. The model takes into account the familial
        dependence defined by the pedigree structure by considering
        that a class of a child depends on his parents classes via
        triplet-transition probabilities of the classes. The package
        handles the case where measurements are available on all
        subjects and the case where measurements are available only on
        symptomatic (i.e. affected) subjects. Distributions for
        discrete (or ordinal) and continuous data are currently
        implemented. The package can deal with missing data.
	"""
	
	homepage = "https://CRAN.R-project.org/package=LCAextend"
	cran = "LCAextend" 

	version("1.3", md5="7815da8c5af3d8094b35aaa901dda47e")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-kinship2", type=("build", "run"))
