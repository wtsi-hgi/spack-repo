# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensory(RPackage):
	"""Simultaneous Model-Based Clustering and Imputation via a
Progressive Expectation-Maximization Algorithm

	Contains the function CUUimpute() which performs model-based clustering and imputation simultaneously.
	"""
	
	cran = "sensory" 

	version("1.1", md5="4c94eacbdde6af5edb6c811818cb84a2")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.2.2:", type=("build", "run"))
