# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcvcomp(RPackage):
	"""Comparison of Variance - Covariance Patterns

	Comparison of variance - covariance patterns using relative principal component analysis (relative eigenanalysis), as described in Le Maitre and Mitteroecker (2019) <doi:10.1111/2041-210X.13253>. Also provides functions to compute group covariance matrices, distance matrices, and perform proportionality tests. A worked sample on the body shape of cichlid fishes is included, based on the dataset from Kerschbaumer et al. (2013) <doi:10.5061/dryad.fc02f>. 
	"""
	
	cran = "vcvComp" 

	version("1.0.2", md5="802c3ae93760f71ab4c0dbd831e2d8c1")

	depends_on("r@3.6:", type=("build", "run"))
