# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatetimeutils(RPackage):
	"""Utilities for Dates and Times

	Utilities for handling dates and times, such
   as selecting particular days of the week or month,
   formatting timestamps as required by RSS feeds, or
   converting timestamp representations of other software
   (such as 'MATLAB' and 'Excel') to R. The package is
   lightweight (no dependencies, pure R implementations) and
   relies only on R's standard classes to represent dates
   and times ('Date' and 'POSIXt'); it aims to provide
   efficient implementations, through vectorisation and the
   use of R's native numeric representations of timestamps
   where possible.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/datetimeutils/"
	cran = "datetimeutils" 

	version("0.6-3", md5="057ff0476d6a96d6b4c6b090e8e4dc0b")

