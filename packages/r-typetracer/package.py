# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTypetracer(RPackage):
	"""Trace Function Parameter Types

	The 'R' language includes a set of defined types, but the language
    itself is "absurdly dynamic" (Turcotte & Vitek (2019)
    <doi:10.1145/3340670.3342426>), and lacks any way to specify which types are
    expected by any expression. The 'typetracer' package enables code to be
    traced to extract detailed information on the properties of parameters
    passed to 'R' functions. 'typetracer' can trace individual functions or
    entire packages.
	"""
	
	homepage = "https://github.com/mpadge/typetracer"
	cran = "typetracer" 

	version("0.2.2", md5="2ec3a9778fb68d644562c16efe2b556e")

	depends_on("r-brio", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
