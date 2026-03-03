# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQtwacademic(RPackage):
	"""'Quarto' Website Templates for Academics

	Provides three 'Quarto' website templates as an R project, which are commonly used by academics.
    Templates for personal websites and course/workshop websites are included, as well as a template with minimal content for customization.
	"""
	
	homepage = "https://andreaczhang.github.io/qtwAcademic/"
	cran = "qtwAcademic" 

	version("2022.12.13", md5="dfa81396a58a043ed8d774d82106f6cb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
