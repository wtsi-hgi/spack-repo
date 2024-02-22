# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsioheaders(RPackage):
	"""'Asio' C++ Header Files

	'Asio' is a cross-platform C++ library for network and low-level
 I/O programming that provides developers with a consistent asynchronous model
 using a modern C++ approach. It is also included in Boost but requires linking
 when used with Boost. Standalone it can be used header-only (provided a recent
 compiler). 'Asio' is written and maintained by Christopher M. Kohlhoff, and
 released under the 'Boost Software License', Version 1.0.
	"""
	
	homepage = "https://github.com/eddelbuettel/asioheaders"
	cran = "AsioHeaders" 

	version("1.22.1-2", md5="7e7f8f45115ba4e62334b225ee859cb0")

