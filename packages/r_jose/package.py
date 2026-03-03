# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJose(RPackage):
	"""JavaScript Object Signing and Encryption

	Read and write JSON Web Keys (JWK, rfc7517), generate and verify JSON
    Web Signatures (JWS, rfc7515) and encode/decode JSON Web Tokens (JWT, rfc7519).
    These standards provide modern signing and encryption formats that are natively
    supported by browsers via the JavaScript WebCryptoAPI, and used by services 
    like OAuth 2.0, LetsEncrypt, and Github Apps.
	"""
	
	homepage = "https://datatracker.ietf.org/wg/jose/documents/"
	cran = "jose" 

	version("1.2.0", md5="977518b8c7369d6cac8507a86038df67")

	depends_on("r-openssl@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
