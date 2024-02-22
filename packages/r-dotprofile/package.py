# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotprofile(RPackage):
	"""Create and Manage Configuration Profiles

	A toolbox to create and manage metadata files and
    configuration profiles: files used to configure the parameters and
    initial settings for some computer programs.
	"""
	
	homepage = "https://github.com/jeanmathieupotvin/dotprofile"
	cran = "dotprofile" 

	version("0.0.1", md5="0611a3f8f9ca12e3e2d0a6deb08e3377")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
