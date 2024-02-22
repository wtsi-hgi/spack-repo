# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatnetCommon(RPackage):
	"""Common R Scripts and Utilities Used by the Statnet Project Software.

	Non-statistical utilities used by the software developed by the Statnet
	Project. They may also be of use to others."""

	cran = "statnet.common"

	version("4.9.0", md5="85503e6c3fdaae2040a8c872fcbd8ad6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
