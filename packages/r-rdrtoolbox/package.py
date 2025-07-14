# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdrtoolbox(RPackage):
	"""A package for nonlinear dimension reduction with Isomap and LLE.

	A package for nonlinear dimension reduction using the Isomap and LLE algorithm. It also includes a routine for computing the Davis-Bouldin-Index for cluster validation, a plotting tool and a data generator for microarray gene expression data and for the Swiss Roll dataset.
	"""
	
	bioc = "RDRToolbox"

	version("1.58.0", commit="f6af32b2ba6c6125ee8d280dd6157cc0ea5b4b04")
	version("1.52.0", commit="5b7002a461da2ee99963d16ca643f1122da87ac4")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
