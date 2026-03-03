# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGData(RPackage):
	"""Delayed-Data Packages

	Create and maintain delayed-data packages (ddp's).  Data stored in
  a ddp are available on demand, but do not take up memory until requested.
  You attach a ddp with g.data.attach(), then read from it and assign to it in
  a manner similar to S-PLUS, except that you must run g.data.save() to
  actually commit to disk.
	"""
	
	cran = "g.data" 

	version("2.4.1", md5="6556c0a1b0af4b237188e011460711b4")

