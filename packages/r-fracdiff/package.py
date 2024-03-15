# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFracdiff(RPackage):
	"""Fractionally Differenced ARIMA aka ARFIMA(P,d,q) Models.

	Maximum likelihood estimation of the parameters of a fractionally
	differenced ARIMA(p,d,q) model (Haslett and Raftery, Appl.Statistics,
	1989); including inference and basic methods.  Some alternative algorithms
	to estimate "H"."""

	cran = "fracdiff"

	license("GPL-2.0-or-later")

	version("1.5-3", md5="f709c0a691bc7287bb5ab1f014885a4f")

