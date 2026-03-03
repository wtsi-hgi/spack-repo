# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTarchetypes(RPackage):
	"""Archetypes for Targets

	Function-oriented Make-like declarative pipelines for
  Statistics and data science are supported in the 'targets' R package.
  As an extension to 'targets', the 'tarchetypes' package provides
  convenient user-side functions to make 'targets' easier to use.
  By establishing reusable archetypes for common kinds of
  targets and pipelines, these functions help express complicated
  reproducible pipelines concisely and compactly.
  The methods in this package were influenced by the 'drake' R package
  by Will Landau (2018) <doi:10.21105/joss.00550>.
	"""
	
	homepage = "https://docs.ropensci.org/tarchetypes/"
	cran = "tarchetypes" 

	version("0.8.0", md5="91c7a481e98dd3b14b780fd45324e232")
	version("0.7.12", md5="39bb3bb543aae37e6ced6fdad833825e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-digest@0.6.25:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fs@1.4.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-targets@1.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.3.4:", type=("build", "run"))
	depends_on("r-withr@2.1.2:", type=("build", "run"))
