# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniset(RPackage):
	"""Dynamic Settings File

	Any package (subsequently called 'target package') is enabled to provide its users an easily accessible, user-friendly and human readable text file where key=value pairs (used by functions defined in the target package) can be saved. This settings file lives in a location defined by the user of the target package, and its user-defined values remain unchanged even when the author of the target package is introducing or deleting keys, or when the target package is updated or re-installed. 
	"""
	
	homepage = "https://bpollner.github.io/uniset/"
	cran = "uniset" 

	version("0.3.1", md5="eb19ab1a48311c13196c3d6a9ad2edb3")

	depends_on("r@3.3.2:", type=("build", "run"))
	depends_on("r-easycsv", type=("build", "run"))
