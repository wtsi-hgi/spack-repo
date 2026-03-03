# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollections(RPackage):
	"""High Performance Container Data Types

	Provides high performance container data types such
    as queues, stacks, deques, dicts and ordered dicts. Benchmarks
    <https://randy3k.github.io/collections/articles/benchmark.html> have
    shown that these containers are asymptotically more efficient than
    those offered by other packages.
	"""
	
	homepage = "https://github.com/randy3k/collections/"
	cran = "collections" 

	version("0.3.7", md5="60632d1a34d64e5aa53165950237d1ee")

