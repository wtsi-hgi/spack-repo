# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFranc(RPackage):
	"""Detect the Language of Text

	With no external dependencies and
    support for 335 languages; all languages spoken by
    more than one million speakers. 'Franc' is a port
    of the 'JavaScript' project of the same name,
    see <https://github.com/wooorm/franc>.
	"""
	
	homepage = "https://github.com/gaborcsardi/franc#readme"
	cran = "franc" 

	version("1.1.4", md5="70ceba316eb7bb80787f57e6e39028a0")

	depends_on("r-jsonlite", type=("build", "run"))
