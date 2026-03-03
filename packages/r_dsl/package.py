# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsl(RPackage):
	"""Distributed Storage and List

	An abstract DList class helps storing large list-type objects in a distributed manner. Corresponding high-level functions and methods for handling distributed storage (DStorage) and lists allows for processing such DLists on distributed systems efficiently. In doing so it uses a well defined storage backend implemented based on the DStorage class.
	"""
	
	cran = "DSL" 

	version("0.1-7", md5="4b7039f50916feae83d2624d2be005dd")

