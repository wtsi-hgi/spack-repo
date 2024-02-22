# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUaparserjs(RPackage):
	"""Parse 'User-Agent' Strings

	Despite there being a section in RFC 7231
    <https://tools.ietf.org/html/rfc7231#section-5.5.3> defining a suggested
    structure for 'User-Agent' headers this data is notoriously difficult
    to parse consistently. Tools are provided that will take in user agent
    strings and return structured R objects. This is a 'V8'-backed package
    based on the 'ua-parser' project <https://github.com/ua-parser>.
	"""
	
	homepage = "https://gitlab.com/hrbrmstr/uaparserjs"
	cran = "uaparserjs" 

	version("0.3.5", md5="4b436bcca25db70d11a57d388a20f414")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
