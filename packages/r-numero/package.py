# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNumero(RPackage):
	"""Statistical Framework to Define Subgroups in Complex Datasets

	High-dimensional datasets that do not exhibit a clear intrinsic clustered structure pose a challenge to conventional clustering algorithms. For this reason, we developed an unsupervised framework that helps scientists to better subgroup their datasets based on visual cues, please see Gao S, Mutter S, Casey A, Makinen V-P (2019) Numero: a statistical framework to define multivariable subgroups in complex population-based datasets, Int J Epidemiology, 48:369-37, <doi:10.1093/ije/dyy113>. The framework includes the necessary functions to construct a self-organizing map of the data, to evaluate the statistical significance of the observed data patterns, and to visualize the results.
	"""
	
	cran = "Numero" 

	version("1.9.6", md5="a42be2b560760f24b923d6c4c7b8f24f")

	depends_on("r-rcpp", type=("build", "run"))
