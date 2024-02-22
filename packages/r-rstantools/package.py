# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstantools(RPackage):
	"""Tools for Developing R Packages Interfacing with 'Stan'.

	Provides various tools for developers of R packages interfacing with 'Stan'
	<https://mc-stan.org>, including functions to set up the required  package
	structure, S3 generics and default methods to unify function naming  across
	'Stan'-based R packages, and vignettes with recommendations for
	developers."""

	cran = "rstantools"

	version("2.4.0", md5="abd80e8b316191cb4e146e09ee9c06fd")

	depends_on("r-desc", type=("build", "run"))
	depends_on("r-rcpp@0.12.16:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
