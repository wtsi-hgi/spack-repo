# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBursts(RPackage):
	"""Markov Model for Bursty Behavior in Streams

	An implementation of Jon Kleinberg's burst detection algorithm (Kleinberg (2003) <doi:10.1023/A:1024940629314>).  Uses an infinite Markov model to detect periods of increased activity in a series of discrete events with known times, and provides a simple visualization of the results.
	"""
	
	cran = "bursts" 

	version("1.0-2", md5="fa08e1af93460502d95a28602144909c")

