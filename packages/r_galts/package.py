# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGalts(RPackage):
	"""Genetic Algorithms and C-Steps Based LTS (Least Trimmed Squares)
Estimation

	Includes the ga.lts() function that estimates
        LTS (Least Trimmed Squares) parameters using genetic algorithms
        and C-steps. ga.lts() constructs a genetic algorithm to form a
        basic subset and iterates C-steps as defined in Rousseeuw and
        van-Driessen (2006) to calculate the cost value of the LTS
        criterion. OLS (Ordinary Least Squares) regression is known to
        be sensitive to outliers. A single outlying observation can
        change the values of estimated parameters. LTS is a resistant
        estimator even the number of outliers is up to half of the
        data. This package is for estimating the LTS parameters with
        lower bias and variance in a reasonable time. Version >=1.3 
        includes the function medmad for fast outlier detection in
        linear regression.
	"""
	
	cran = "galts" 

	version("1.3.2", md5="2499ebb8785ab29c3406af632d32e6ce")

	depends_on("r-genalg", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
