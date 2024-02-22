# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesda(RPackage):
	"""Functions and Datasets for the book "Bayesian Data Analysis"

	Functions for Bayesian Data Analysis, with datasets from
        the book "Bayesian data Analysis (second edition)" by Gelman,
        Carlin, Stern and Rubin. Not all datasets yet, hopefully
        completed soon.
	"""
	
	cran = "BayesDA" 

	version("2012.04-1", md5="fdf97942a76b33fa87588a267068501c")

	depends_on("r@2.2:", type=("build", "run"))
