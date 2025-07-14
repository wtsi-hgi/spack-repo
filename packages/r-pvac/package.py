# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvac(RPackage):
	"""PCA-based gene filtering for Affymetrix arrays

	The package contains the function for filtering genes by the proportion of variation accounted for by the first principal component (PVAC).
	"""
	
	bioc = "pvac"

	version("1.56.0", commit="c1db05d1306dfed3a4ae3140e1c38de5744e8a4e")
	version("1.50.0", commit="66f569fd60dde19666a27a23a20d61f3300986b5")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-affy@1.20:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
