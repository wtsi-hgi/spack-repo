# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThor(RPackage):
	"""Interface to 'LMDB'

	Key-value store, implemented as a wrapper around 'LMDB';
    the "lightning memory-mapped database" <https://www.symas.com/lmdb>.
    'LMDB' is a transactional key value store that uses a memory map
    for efficient access.  This package wraps the entire 'LMDB'
    interface (except duplicated keys), and provides objects for
    transactions and cursors.
	"""
	
	homepage = "https://github.com/richfitz/thor"
	cran = "thor" 

	version("1.1.5", md5="1b6da5a10eb6ba77c2b5295bd971807f")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-storr", type=("build", "run"))
