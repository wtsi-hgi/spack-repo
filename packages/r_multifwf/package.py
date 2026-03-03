# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultifwf(RPackage):
	"""Read Fixed Width Format Files Containing Lines of Different Type

	Read a table of fixed width formatted data of different types into
    a data.frame for each type.
	"""
	
	homepage = "https://github.com/prontog/multifwf"
	cran = "multifwf" 

	version("0.2.2", md5="c9051df5b202fed8f4ad5f17edbf33bc")

	depends_on("r@3.1.1:", type=("build", "run"))
