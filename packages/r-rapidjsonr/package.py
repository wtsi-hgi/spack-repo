# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapidjsonr(RPackage):
	"""'Rapidjson' C++ Header Files.

	Provides JSON parsing capability through the 'Rapidjson' 'C++' header-only
	library."""

	cran = "rapidjsonr"

	license("MIT")

	version("1.2.0", md5="92b93b896fc9b288d4cb7a32def81144")

