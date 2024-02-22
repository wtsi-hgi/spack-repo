# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmemorySri(RPackage):
	"""A shared resource interface for Bigmemory Project packages.

	This package provides a shared resource interface for the bigmemory and
	synchronicity packages."""

	cran = "bigmemory.sri"

	version("0.1.8", md5="cc643b29f763b8e1381f5130023861c4")

