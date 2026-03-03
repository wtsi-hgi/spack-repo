# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvclass(RPackage):
	"""P-Values for Classification

	Computes nonparametric p-values for the potential class
        memberships of new observations as well as cross-validated
        p-values for the training data. The p-values are based on
        permutation tests applied to an estimated Bayesian likelihood
        ratio, using a plug-in statistic for the Gaussian model, 'k
        nearest neighbors', 'weighted nearest neighbors' or
        'penalized logistic regression'.
        Additionally, it provides graphical displays and quantitative
        analyses of the p-values.
	"""
	
	cran = "pvclass" 

	version("1.4", md5="f3a49d1d6730d342e754e157718643a2")

	depends_on("r-matrix", type=("build", "run"))
