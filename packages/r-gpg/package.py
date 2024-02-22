# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpg(RPackage):
	"""GNU Privacy Guard for R

	Bindings to GnuPG for working with OpenGPG (RFC4880) cryptographic 
    methods. Includes utilities for public key encryption, creating and verifying
    digital signatures, and managing your local keyring. Some functionality 
    depends on the version of GnuPG that is installed on the system. On Windows
    this package can be used together with 'GPG4Win' which provides a GUI for 
    managing keys and entering passphrases.
	"""
	
	homepage = "https://github.com/jeroen/gpg"
	cran = "gpg" 

	version("1.2.9", md5="0742a9b2a631f710f9b6324a1273e971")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("gpgme", type=("build", "link", "run"))
