# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUsl(RPackage):
	"""Analyze System Scalability with the Universal Scalability Law

	The Universal Scalability Law (Gunther 2007)
    <doi:10.1007/978-3-540-31010-5> is a model to predict hardware and
    software scalability. It uses system capacity as a function of load to
    forecast the scalability for the system.
	"""
	
	cran = "usl" 

	version("3.0.3", md5="d05ddd3a682abd636fda34d477755ea8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlsr", type=("build", "run"))
