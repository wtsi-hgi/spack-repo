# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPulsar(RPackage):
	"""Parallel Utilities for Lambda Selection along a Regularization
Path

	Model selection for penalized graphical models using the Stability Approach to Regularization Selection ('StARS'), with options for speed-ups including Bounded StARS (B-StARS), batch computing, and other stability metrics (e.g., graphlet stability G-StARS). Christian L. Müller, Richard Bonneau, Zachary Kurtz (2016) <arXiv:1605.07072>.
	"""
	
	homepage = "https://github.com/zdk123/pulsar"
	cran = "pulsar" 

	version("0.3.11", md5="a853ab7dee073461b8ff59ae084a86e4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix@1.5:", type=("build", "run"))
