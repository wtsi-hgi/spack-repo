# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRavenRdf(RPackage):
	"""An R Interface for Raven DataFrames (Beta0)

	Provides an I/O interface between R data.frames and
    Raven DataFrames. Defines functions to both read and write DataFrame
    files, as well as serialize/deserialize data.frames/DataFrames.
	"""
	
	homepage = "https://github.com/raven-computing/rdf"
	cran = "raven.rdf" 

	version("0.2.0", md5="57d222759aa2b64a7f8ab506e1cdca28")

	depends_on("r@3.5:", type=("build", "run"))
