# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAod(RPackage):
	"""Analysis of Overdispersed Data.

	Provides a set of functions to analyse overdispersed counts or proportions.
	Most of the methods are already available elsewhere but are scattered in
	different packages. The proposed functions should be considered as
	complements to more sophisticated methods such as generalized estimating
	equations (GEE) or generalized linear mixed effect models (GLMM)."""

	cran = "aod"

	license("GPL-2.0-or-later")

	version("1.3.3", md5="1be0359bcffcbec8fa4bbbd78e4df84a")

	depends_on("r@2.10:", type=("build", "run"))
