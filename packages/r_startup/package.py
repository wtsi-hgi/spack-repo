# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStartup(RPackage):
	"""Friendly R Startup Configuration

	Adds support for R startup configuration via '.Renviron.d' and '.Rprofile.d' directories in addition to '.Renviron' and '.Rprofile' files.  This makes it possible to keep private / secret environment variables separate from other environment variables.  It also makes it easier to share specific startup settings by simply copying a file to a directory.
	"""
	
	homepage = "https://henrikbengtsson.github.io/startup/"
	cran = "startup" 

	version("0.21.0", md5="64234c3083e12de6b9c1a6a679f4847b")

	depends_on("r@2.14:", type=("build", "run"))
