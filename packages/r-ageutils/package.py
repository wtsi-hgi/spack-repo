# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgeutils(RPackage):
	"""Collection of Functions for Working with Age Intervals

	Provides a collection of efficient functions for working with
  individual ages and corresponding intervals. These include functions for
  efficient conversion from an age to an interval, aggregation of ages with
  associated counts in to intervals and the splitting of interval counts based
  on specified age distributions.
	"""
	
	homepage = "https://timtaylor.github.io/ageutils/"
	cran = "ageutils" 

	version("0.0.1", md5="728b436ffe6d52f074f04d16eca351dd")

	depends_on("r@3.5:", type=("build", "run"))
