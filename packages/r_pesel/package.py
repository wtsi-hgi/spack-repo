# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPesel(RPackage):
	"""Automatic Estimation of Number of Principal Components in PCA

	Automatic estimation of number of principal components in PCA
    with PEnalized SEmi-integrated Likelihood (PESEL). See Piotr Sobczyk, Malgorzata Bogdan, Julie Josse
    "Bayesian dimensionality reduction with PCA using penalized semi-integrated likelihood"
    (2017) <doi:10.1080/10618600.2017.1340302>.
	"""
	
	homepage = "https://github.com/psobczyk/pesel"
	cran = "pesel" 

	version("0.7.5", md5="2fb4da6794a4702603c7c606ae4d1f76")

	depends_on("r@3.1.3:", type=("build", "run"))
