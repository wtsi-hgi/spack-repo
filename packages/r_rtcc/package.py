# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcc(RPackage):
	"""Detecting Trait Clustering in Environmental Gradients

	The Randomized Trait Community Clustering method (Triado-Margarit et al., 2019,
    <doi:10.1038/s41396-019-0454-4>) is a statistical approach which allows to determine whether
    if an observed trait clustering pattern is related to an increasing environmental constrain.
    The method 1) determines whether exists or not a trait clustering on the sampled communities
    and 2) assess if the observed clustering signal is related or not to an increasing environmental
    constrain along an environmental gradient. Also, when the effect of the environmental gradient
    is not linear, allows to determine consistent thresholds on the community assembly based on trait-values.
	"""
	
	cran = "RTCC" 

	version("0.1.1", md5="21596e46f8fa9085c6d7cfc38744b994")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
