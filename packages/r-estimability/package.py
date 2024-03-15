# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstimability(RPackage):
	"""Tools for Assessing Estimability of Linear Predictions.

	Provides tools for determining estimability of linear functions of
	regression coefficients, and 'epredict' methods that handle non-estimable
	cases correctly. Estimability theory is discussed in many linear-models
	textbooks including Chapter 3 of Monahan, JF (2008), "A Primer on Linear
	Models", Chapman and Hall (ISBN 978-1-4200-6201-4)."""

	cran = "estimability"

	license("GPL-3.0-or-later")

	version("1.5", md5="36a7cd52f48a9421d8152cc2e814f603")

	depends_on("r@4.3:", type=("build", "run"))
