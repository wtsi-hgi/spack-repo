# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultcompview(RPackage):
	"""Visualizations of Paired Comparisons.

	Convert a logical vector or a vector of p-values or a correlation,
	difference, or distance matrix into a display identifying the pairs for
	which the differences were not significantly different. Designed for use in
	conjunction with the output of functions like TukeyHSD, dist{stats},
	simint, simtest, csimint, csimtest{multcomp}, friedmanmc,
	kruskalmc{pgirmess}."""

	cran = "multcompView"
	version("0.1-9", sha256="1f3993e9d51f3c7a711a881b6a20081a85ffab60c27828ceb3640a6b4c887397")
	version("0.1-8", sha256="123d539172ad6fc63d83d1fc7f356a5ed7b691e7803827480118bebc374fd8e5")
	version("0.1-7", sha256="f1dc100d602a82694e97bf4329af7220b8395b17340d4047d0f2bbd7dbb0eea1")
	version("0.1-5", sha256="2b42d6c701016c59148ede73e357751459978fecbde4a1f174d1f7873bdecf6d")
	version("0.1-3", sha256="20b81c75eeaf546bcff5afaa7d1c4e2e5f834421faa3ea609f85217ba1787b66")
	version("0.1-2", sha256="702f54d20fa107eeb75c655ce35588d0c6b8d2b9d9e4bc6db95edb61d2f895a3")
	version("0.1-10", md5="7c183f073461e938ceef476dd4f50c81")
	version("0.1-0", sha256="6d85f09d14134cf351becd7a7a9e195278fc1d739a95f709c5135d395797ace6")

