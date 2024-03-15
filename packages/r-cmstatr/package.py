# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmstatr(RPackage):
	"""Statistical Methods for Composite Material Data

	An implementation of the statistical methods commonly
  used for advanced composite materials in aerospace applications.
  This package focuses on calculating basis values (lower tolerance
  bounds) for material strength properties, as well as performing the
  associated diagnostic tests. This package provides functions for
  calculating basis values assuming several different distributions,
  as well as providing functions for non-parametric methods of computing
  basis values. Functions are also provided for testing the hypothesis
  that there is no difference between strength and modulus data from an
  alternate sample and that from a "qualification" or "baseline" sample.
  For a discussion of these statistical methods and their use, see the
  Composite Materials Handbook, Volume 1 (2012, ISBN: 978-0-7680-7811-4).
  Additional details about this package are available in the paper by
  Kloppenborg (2020, <doi:10.21105/joss.02265>).
	"""
	
	homepage = "https://www.cmstatr.net/"
	cran = "cmstatr" 

	version("0.9.3", md5="51f00b72f5b9d4f1acc5df11425f90fa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
