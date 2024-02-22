# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RX13binary(RPackage):
	"""Provide the 'x13ashtml' Seasonal Adjustment Binary

	The US Census Bureau provides a seasonal adjustment program now
 called 'X-13ARIMA-SEATS' building on both earlier programs called X-11 and
 X-12 as well as the SEATS program by the Bank of Spain. The US Census Bureau
 offers both source and binary versions -- which this package integrates for
 use by other R packages.
	"""
	
	homepage = "https://github.com/x13org/x13binary"
	cran = "x13binary" 

	version("1.1.60", md5="538d017a126195efd14f1a75492cfae3")

