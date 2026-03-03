# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcrypt(RPackage):
	"""'Blowfish' Password Hashing Algorithm

	Bindings to the 'blowfish' password hashing algorithm derived from
    the 'OpenBSD' implementation.
	"""
	
	homepage = "https://github.com/jeroen/bcrypt"
	cran = "bcrypt" 

	version("1.1", md5="2993d2be0f7c1bc44f0ca20a1f49d977")

	depends_on("r-openssl", type=("build", "run"))
