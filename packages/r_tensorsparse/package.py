# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorsparse(RPackage):
	"""Multiway Clustering via Tensor Block Models

	Implements the multiway sparse clustering approach of M. Wang and Y. Zeng, "Multiway clustering via tensor block models". Advances in Neural Information Processing System 32 (NeurIPS), 715-725, 2019.
	"""
	
	cran = "tensorsparse" 

	version("3.0", md5="e88b0f0317b9e1b26bcf6440d2c7d3a8")

