# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAprof(RPackage):
	"""Amdahl's Profiler, Directed Optimization Made Easy

	Assists the evaluation of whether and
    where to focus code optimization, using Amdahl's law and visual aids
    based on line profiling. Amdahl's profiler organizes profiling output
    files (including memory profiling) in a visually appealing way.
    It is meant to help to balance development
    vs. execution time by helping to identify the most promising sections
    of code to optimize and projecting potential gains. The package is
    an addition to R's standard profiling tools and is not a wrapper for them.
	"""
	
	homepage = "http://github.com/MarcoDVisser/aprof"
	cran = "aprof" 

	version("0.4.1", md5="db240768e25de08a25de85f1aec45f5c")

	depends_on("r-testthat", type=("build", "run"))
