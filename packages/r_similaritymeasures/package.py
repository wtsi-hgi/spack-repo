# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimilaritymeasures(RPackage):
	"""Trajectory Similarity Measures

	Functions to run and assist four
  different similarity measures. The similarity
  measures included are: longest common
  subsequence (LCSS), Frechet distance, edit distance
  and dynamic time warping (DTW). Each of these
  similarity measures can be calculated from two
  n-dimensional trajectories, both in matrix form.
	"""
	
	cran = "SimilarityMeasures" 

	version("1.4", md5="32b53760a59b714ff4ab0b7512dfae7c")

