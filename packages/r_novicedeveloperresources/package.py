# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNovicedeveloperresources(RPackage):
	"""Resources to Assist Novice Developers

	Assist novice developers when preparing a single package or a set of integrated packages to submit to CRAN. Automate the following individual or batch processing: check local source packages;  build local .tar.gz source files; install packages from local .tar.gz files; detect conflicts between function names in the environment.
	"""
	
	cran = "NoviceDeveloperResources" 

	version("1.1.0", md5="02fc81b7a293f12ace9ebdbed3ba33e8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
