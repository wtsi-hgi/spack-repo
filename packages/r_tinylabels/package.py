# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinylabels(RPackage):
	"""Lightweight Variable Labels

	Assign, extract, or remove variable labels from R vectors.
  Lightweight and dependency-free.
	"""
	
	homepage = "https://github.com/mariusbarth/tinylabels"
	cran = "tinylabels" 

	version("0.2.4", md5="ff1a6b76a4f40793576644679a400616")

