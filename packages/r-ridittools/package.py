# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRidittools(RPackage):
	"""Useful Functions for Ridit Analysis

	Functions to compute ridit scores of vectors, compute mean ridits
  and their standard errors for vectors compared to a reference vector,
  as described in Fleiss (1981, ISBN:0-471-06428-9), and compute
  means/SEs for multiple groups in matrices. Data can be either
  counts or proportions. Emphasis is on ridit analysis of ordered categorical
  data such as Likert items and pain-rating scales.
	"""
	
	cran = "ridittools" 

	version("0.1", md5="3f350f5077550c3213e9c99a85852478")

