# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtp(RPackage):
	"""One Time Password Generation and Verification

	Generating and validating One-time Password based on 
    Hash-based Message Authentication Code (HOTP) 
    and Time Based One-time Password (TOTP)
    according to RFC 4226 <https://datatracker.ietf.org/doc/html/rfc4226> and
    RFC 6238 <https://datatracker.ietf.org/doc/html/rfc6238>.
	"""
	
	homepage = "https://github.com/randy3k/otp"
	cran = "otp" 

	version("0.1.1", md5="df6cf9895f6977305aa1c6ced80c2555")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-base64url", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
