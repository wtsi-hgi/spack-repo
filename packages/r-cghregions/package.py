# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghregions(RPackage):
	"""Dimension Reduction for Array CGH Data with Minimal Information Loss.

	Dimension Reduction for Array CGH Data with Minimal Information Loss
	"""
	
	bioc = "CGHregions" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CGHregions_1.60.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CGHregions/CGHregions_1.60.0.tar.gz"]

	version("1.66.0", tag="RELEASE_3_21")
	version("1.60.0", sha256="cebd9a63726abf5526ed2379866d71342618f7b68716eefb38ececea31539cb5")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-cghbase", type=("build", "run"))
