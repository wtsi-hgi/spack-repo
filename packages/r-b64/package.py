# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RB64(RPackage):
	"""Fast and Vectorized Base 64 Engine

	Provides a fast, lightweight, and vectorized base 64 engine
    to encode and decode character and raw vectors as well as files stored
    on disk.  Common base 64 alphabets are supported out of the box
    including the standard, URL-safe, bcrypt, crypt, 'BinHex', and
    IMAP-modified UTF-7 alphabets. Custom engines can be created to
    support unique base 64 encoding and decoding needs.
	"""
	
	cran = "b64" 

	version("0.1.0", md5="69352a0f658b01b3a6a9f2270a08495d", url="https://cran.r-project.org/src/contrib/b64_0.1.0.tar.gz")

	depends_on("r-blob", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
