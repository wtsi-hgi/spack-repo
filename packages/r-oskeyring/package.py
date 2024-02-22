# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROskeyring(RPackage):
	"""Raw System Credential Store Access from R

	Aims to support all features of the system credential store,
    including non-portable ones. Supports 'Keychain' on 'macOS', and
    'Credential Manager' on 'Windows'. See the 'keyring' package if you
    need a portable 'API'.
	"""
	
	homepage = "https://github.com/r-lib/oskeyring#readme"
	cran = "oskeyring" 

	version("0.1.6", md5="d6225c3ddbf92c7b4b4eea596cd756dc")

	depends_on("r@3.4:", type=("build", "run"))
