# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSensrivastava(RPackage):
	"""Datasets from Sen & Srivastava

	Collection of datasets from Sen & Srivastava: "Regression
        Analysis, Theory, Methods and Applications", Springer.  Sources
        for individual data files are more fully documented in the
        book.
	"""
	
	cran = "SenSrivastava" 

	version("2015.6.25.1", md5="5169dc05c9139a1fdfbaf1f5eb5fc88d")

	depends_on("r@2.10:", type=("build", "run"))
