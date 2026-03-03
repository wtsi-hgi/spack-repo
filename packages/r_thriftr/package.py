# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThriftr(RPackage):
	"""Apache Thrift Client Server

	Pure R implementation of Apache Thrift.
    This library doesn't require any code generation.
    To learn more about Thrift go to <https://thrift.apache.org>.
	"""
	
	homepage = "https://github.com/systemincloud/thriftr"
	cran = "thriftr" 

	version("1.1.7", md5="e97db8206c98425dec03d9430342da07")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rly@1.7.4:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
