# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVgam(RPackage):
	"""Vector Generalized Linear and Additive Models.

	An implementation of about 6 major classes of statistical regression
	models. The central algorithm is Fisher scoring and iterative reweighted
	least squares. At the heart of this package are the vector generalized
	linear and additive model (VGLM/VGAM) classes. VGLMs can be loosely thought
	of as multivariate GLMs. VGAMs are data-driven VGLMs that use smoothing.
	The book "Vector Generalized Linear and Additive Models: With an
	Implementation in R" (Yee, 2015) <DOI:10.1007/978-1-4939-2818-7> gives
	details of the statistical framework and the package. Currently only
	fixed-effects models are implemented. Many (150+) models and distributions
	are estimated by maximum likelihood estimation (MLE) or penalized MLE. The
	other classes are RR-VGLMs (reduced-rank VGLMs), quadratic RR-VGLMs,
	reduced-rank VGAMs, RCIMs (row-column interaction models)---these classes
	perform constrained and unconstrained quadratic ordination (CQO/UQO) models
	in ecology, as well as constrained additive ordination (CAO). Hauck-Donner
	effect detection is implemented. Note that these functions are subject to
	change; see the NEWS and ChangeLog files for latest changes."""

	cran = "VGAM"

	version("1.1-10", md5="4775c04874f72d7920d38462f321cdf9")

	depends_on("r@4:", type=("build", "run"))
