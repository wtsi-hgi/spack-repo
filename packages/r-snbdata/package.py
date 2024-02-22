# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnbdata(RPackage):
	"""Download Data from the Swiss National Bank (SNB)

	Download data (tables and datasets) from the Swiss
     National Bank (SNB; <https://www.snb.ch/en>), the Swiss
     central bank.  The package is lightweight and comes with few
     dependencies; suggested packages are used only if data is to
     be transformed into particular data structures, for instance
     into 'zoo' objects.  Downloaded data can optionally be
     cached, to avoid repeated downloads of the same files.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/SNBdata/"
	cran = "SNBdata" 

	version("0.2.1", md5="fc24cdd45f5d8086767fbcac8a2d1a02")

