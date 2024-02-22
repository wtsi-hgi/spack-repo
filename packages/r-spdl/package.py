# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpdl(RPackage):
	"""Easier Use of 'RcppSpdlog' Functions via Wrapper

	Logging functions in 'RcppSpdlog' provide access to the logging
 functionality from the 'spdlog' 'C++' library. This package offers shorter convenience
 wrappers for the 'R' functions which match the 'C++' functions, namely via, say,
 'spdl::debug()' at the debug level. The actual formatting is done by the
 'fmt::format()' function from the 'fmtlib' library (that is also 'std::format()'
 in 'C++20' or later).
	"""
	
	homepage = "https://github.com/eddelbuettel/spdl"
	cran = "spdl" 

	version("0.0.5", md5="7bb2627f772de9482c551245b79df52a")

	depends_on("r-rcppspdlog@0.0.13:", type=("build", "run"))
