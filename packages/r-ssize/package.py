# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsize(RPackage):
	"""Estimate Microarray Sample Size

	Functions for computing and displaying sample size information for gene expression arrays.
	"""
	
	bioc = "ssize"

	version("1.82.0", commit="cc6ab98cd54511fe39bd6b98985f67f8d2ec63ae")
	version("1.76.0", commit="308c3314eaaa012466d86fcdf94f1721c9a0f0dc")

	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
