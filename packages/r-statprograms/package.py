# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatprograms(RPackage):
	"""Graduate Statistics Program Datasets

	A small collection of data on graduate statistics programs from the United States.
	"""
	
	homepage = "http://brettklamer.com/work/statprograms/"
	cran = "statprograms" 

	version("0.2.0", md5="c876078c7c406fb21420b3e6bc2ec5c2")

	depends_on("r@2.10:", type=("build", "run"))
