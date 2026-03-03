# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRechonest(RPackage):
	"""R Interface to Echo Nest API

	The 'Echo nest' <http://the.echonest.com> is the industry's leading
    music intelligence company, providing developer with deepest understanding of
    music content and music fans. This package can be used to access artist's data
    including songs, blogs, news, reviews etc. Song's data including audio summary,
    style, danceability, tempo etc can also be accessed.
	"""
	
	homepage = "https://github.com/mukul13/rechonest"
	cran = "rechonest" 

	version("1.2", md5="acd719d6e686f3a4494446e54ad8291d")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
