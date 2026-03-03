# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDipw(RPackage):
	"""Debiased Inverse Propensity Score Weighting

	Estimation of the average treatment effect when controlling for
    high-dimensional confounders using debiased inverse propensity score
    weighting (DIPW). DIPW relies on the propensity score following a sparse
    logistic regression model, but the regression curves are not required to be
    estimable. Despite this, our package also allows the users to estimate 
    the regression curves and take the estimated curves as input to our
    methods. Details of the methodology can be found in Yuhao Wang and
    Rajen D. Shah (2020) "Debiased Inverse Propensity Score Weighting for
    Estimation of Average Treatment Effects with High-Dimensional Confounders"
    <arXiv:2011.08661>. The package relies on the optimisation
    software 'MOSEK' <https://www.mosek.com/> which must be installed separately;
    see the documentation for 'Rmosek'. 
	"""
	
	cran = "dipw" 

	version("0.1.0", md5="18538350f570a16704000796ad7d6d42")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rmosek", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
