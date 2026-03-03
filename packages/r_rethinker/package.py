# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRethinker(RPackage):
	"""RethinkDB Client

	Simple, native 'RethinkDB' client.
	"""
	
	homepage = "https://github.com/mbq/rethinker"
	cran = "rethinker" 

	version("1.1.0", md5="902ec0d31324735b7d35f30ae4ee9f5e")

	depends_on("r-rjson", type=("build", "run"))
