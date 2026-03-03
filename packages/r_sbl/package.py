# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbl(RPackage):
	"""Sparse Bayesian Learning for QTL Mapping and Genome-Wide
Association Studies

	Implements sparse Bayesian learning method for QTL mapping and genome-wide association studies.
	"""
	
	cran = "sbl" 

	version("0.1.0", md5="5f08a473b6d62f58085bf49594d126ba")

	depends_on("r@2.10:", type=("build", "run"))
