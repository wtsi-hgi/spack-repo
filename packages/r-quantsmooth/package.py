# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantsmooth(RPackage):
	"""Quantile smoothing and genomic visualization of array data

	Implements quantile smoothing as introduced in: Quantile smoothing of array CGH data; Eilers PH, de Menezes RX; Bioinformatics. 2005 Apr 1;21(7):1146-53.
	"""
	
	bioc = "quantsmooth"

	version("1.74.0", commit="09529b62dc2d3fcfd60bc6ee121a91261312bc50")
	version("1.68.0", commit="ac99e3f8bd62e5237072efe3d25f9ac31da03909")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
