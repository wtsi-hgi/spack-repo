# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotenv(RPackage):
	"""Load Environment Variables from '.env'

	Load configuration from a '.env' file, that is
    in the current working directory, into environment variables.
	"""
	
	homepage = "https://github.com/gaborcsardi/dotenv"
	cran = "dotenv" 

	version("1.0.3", md5="dd185743606b11664edf3d8f6f177429")

