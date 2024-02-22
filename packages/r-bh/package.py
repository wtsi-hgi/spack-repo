# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBh(RPackage):
	"""Boost C++ Header Files.

	Boost provides free peer-reviewed portable C++ source libraries. A large
	part of Boost is provided as C++ template code which is resolved entirely
	at compile-time without linking. This package aims to provide the most
	useful subset of Boost libraries for template use among CRAN package. By
	placing these libraries in this package, we offer a more efficient
	distribution system for CRAN as replication of this code in the sources of
	other packages is avoided. As of release 1.60.0-2, the following Boost
	libraries are included: 'algorithm' 'any' 'bimap' 'bind' 'circular_buffer'
	'concept' 'config' 'container' 'date'_'time' 'detail' 'dynamic_bitset'
	'exception' 'filesystem' 'flyweight' 'foreach' 'functional' 'fusion'
	'geometry' 'graph' 'heap' 'icl' 'integer' 'interprocess' 'intrusive' 'io'
	'iostreams' 'iterator' 'math' 'move' 'mpl' 'multiprcecision' 'numeric'
	'pending' 'phoenix' 'preprocessor' 'random' 'range' 'smart_ptr' 'spirit'
	'tuple' 'type_trains' 'typeof' 'unordered' 'utility' 'uuid'."""

	cran = "BH"

	version("1.84.0-0", md5="34c6a9cf6213e6e93417b3168c4c84b4")

