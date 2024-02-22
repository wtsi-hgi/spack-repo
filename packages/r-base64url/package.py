# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBase64url(RPackage):
	"""Fast and URL-Safe Base64 Encoder and Decoder

	In contrast to RFC3548, the 62nd character ("+") is replaced with
    "-", the 63rd character ("/") is replaced with "_". Furthermore, the encoder
    does not fill the string with trailing "=". The resulting encoded strings
    comply to the regular expression pattern "[A-Za-z0-9_-]" and thus are
    safe to use in URLs or for file names.
    The package also comes with a simple base32 encoder/decoder suited for
    case insensitive file systems.
	"""
	
	homepage = "https://github.com/mllg/base64url"
	cran = "base64url" 

	version("1.4", md5="0e41f7f53213278d81e2d1fb55b34480")

	depends_on("r-backports@1.1:", type=("build", "run"))
