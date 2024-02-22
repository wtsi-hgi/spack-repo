# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvr(RPackage):
	"""Phylogenetic Eigenvectors Regression and Phylogentic
Signal-Representation Curve

	Estimates (and controls for) phylogenetic signal through phylogenetic eigenvectors regression (PVR) and phylogenetic signal-representation (PSR) curve, along with some plot utilities.
	"""
	
	cran = "PVR" 

	version("0.3", md5="4be5b920c7d382a3444b034a247c671f")

	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
