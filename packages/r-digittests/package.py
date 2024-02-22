# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigittests(RPackage):
	"""Tests for Detecting Irregular Digit Patterns

	Provides statistical tests and support functions for detecting irregular digit patterns in numerical data. The package includes tools for extracting digits at various locations in a number, tests for repeated values, and (Bayesian) tests of digit distributions.
	"""
	
	homepage = "https://koenderks.github.io/digitTests/"
	cran = "digitTests" 

	version("0.1.2", md5="042939d50f5a96f5298d77069167d227")

