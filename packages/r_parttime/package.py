# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParttime(RPackage):
	"""Partial Datetime Handling

	
    Datetimes and timestamps are invariably an imprecise notation, with any
    partial representation implying some amount of uncertainty. To handle this,
    'parttime' provides classes for embedding partial missingness as a central
    part of its datetime classes. This central feature allows for more ergonomic
    use of datetimes for challenging datetime computation, including
    calculations of overlapping date ranges, imputations, and more thoughtful
    handling of ambiguity that arises from uncertain time zones. This package was
    developed first and foremost with pharmaceutical applications in mind, but
    aims to be agnostic to application to accommodate general use cases just as
    conveniently.
	"""
	
	homepage = "https://dgkf.github.io/parttime/"
	cran = "parttime" 

	version("0.1.2", md5="b3d162b52eff8499e4be9f13c3b0ddbb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-vctrs@0.2:", type=("build", "run"))
