# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdwasserstein(RPackage):
	"""Application of Optimal Transport to Functional Data Analysis

	These functions were developed to support statistical analysis on functional covariance operators.
  The package contains functions to:
  - compute 2-Wasserstein distances between Gaussian Processes as in
    Masarotto, Panaretos & Zemel (2019) <doi:10.1007/s13171-018-0130-1>;
  - compute the Wasserstein barycenter (Frechet mean) as in Masarotto,
    Panaretos & Zemel (2019) <doi:10.1007/s13171-018-0130-1>;
  - perform analysis of variance testing procedures for functional
    covariances and tangent space principal component analysis of
    covariance operators as in Masarotto, Panaretos & Zemel (2022)
    <arXiv:2212.04797>.
  - perform a soft-clustering based on the Wasserstein distance where
    functional data are classified based on their covariance structure
    as in Masarotto & Masarotto (2023) <doi:10.1111/sjos.12692>.
	"""
	
	cran = "fdWasserstein" 

	version("1.0", md5="a1800196f886dd194ee995eebfd29106")

	depends_on("r@3.5:", type=("build", "run"))
