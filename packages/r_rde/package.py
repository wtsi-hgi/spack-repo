# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRde(RPackage):
	"""Reproducible Data Embedding

	Allows caching of raw data directly in R code. This allows R
  scripts and R Notebooks to be shared and re-run on a machine without access
  to the original data. Cached data is encoded into an ASCII string that can
  be pasted into R code. When the code is run, the data is automatically
  loaded from the cached version if the original data file is unavailable.
  Works best for small datasets (a few hundred observations).
	"""
	
	homepage = "https://github.com/kloppen/rde"
	cran = "rde" 

	version("0.1.0", md5="a2f9663dda8673b417964ff16b75f908")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clipr", type=("build", "run"))
	depends_on("xclip", type=("build", "link", "run"))
