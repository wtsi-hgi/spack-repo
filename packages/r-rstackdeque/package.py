# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstackdeque(RPackage):
	"""Persistent Fast Amortized Stack and Queue Data Structures

	Provides fast, persistent (side-effect-free) stack, queue and
    deque (double-ended-queue) data structures. While deques include a superset
    of functionality provided by queues, in these implementations queues are
    more efficient in some specialized situations. See the documentation for
    rstack, rdeque, and rpqueue for details.
	"""
	
	homepage = "https://github.com/oneilsh/rstackdeque"
	cran = "rstackdeque" 

	version("1.1.1", md5="af569505475fbed67fd9f4b8a27301d3")

