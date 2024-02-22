# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAion(RPackage):
	"""Archaeological Time Series

	A toolkit for archaeological time series. This package
    provides a system of classes and methods to represent and work with
    archaeological time series. Dates are represented as "rata die" and
    can be converted to (virtually) any calendar defined by Reingold and
    Dershowitz (2018) <doi:10.1017/9781107415058>. This packages offers a
    simple API that can be used by other specialized packages.
	"""
	
	homepage = "https://packages.tesselle.org/aion/"
	cran = "aion" 

	version("1.0.2", md5="80e139b7beb33629f3031858c7cf2117")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-arkhe@1.3:", type=("build", "run"))
