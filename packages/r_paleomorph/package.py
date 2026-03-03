# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaleomorph(RPackage):
	"""Geometric Morphometric Tools for Paleobiology

	Fill missing symmetrical data with mirroring, calculate Procrustes alignments with or without scaling, and compute standard or vector correlation and covariance matrices (congruence coefficients) of 3D landmarks. Tolerates missing data for all analyses.
	"""
	
	homepage = "https://github.com/timcdlucas/paleomorph/"
	cran = "paleomorph" 

	version("0.1.4", md5="cbc8feefe5f5010effa3f936ca23594f")

