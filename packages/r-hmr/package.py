# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmr(RPackage):
	"""Flux Estimation with Static Chamber Data

	Statistical analysis of static chamber concentration data for trace gas flux estimation.
	"""
	
	cran = "HMR" 

	version("1.0.3", md5="c495699dd82e8ab84457142d3bd579b9")

