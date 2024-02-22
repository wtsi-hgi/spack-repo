# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtmlutils(RPackage):
	"""Facilitates Automated HTML Report Creation

	Facilitates automated HTML report creation, in particular
        framed HTML pages and dynamically sortable tables.
	"""
	
	cran = "HTMLUtils" 

	version("0.1.9", md5="dfdfd0071ccdaf1d589c20a8513d9752")

	depends_on("r-r2html", type=("build", "run"))
