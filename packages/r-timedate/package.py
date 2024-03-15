# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimedate(RPackage):
	"""Rmetrics - Chronological and Calendar Objects.

	The 'timeDate' class fulfils the conventions of the ISO 8601 standard as
	well as of the ANSI C and POSIX standards. Beyond these standards it
	provides the "Financial Center" concept which allows to handle data records
	collected in different time zones and mix them up to have always the proper
	time stamps with respect to your personal financial center, or
	alternatively to the GMT reference time. It can thus also handle time
	stamps from historical data records from the same time zone, even if the
	financial centers changed day light saving times at different calendar
	dates."""

	cran = "timeDate"

	version("4032.109", md5="96ed5f3e9a0bd034dfb65dc2a4aff33f")

	depends_on("r@3.6:", type=("build", "run"))
