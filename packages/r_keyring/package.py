# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyring(RPackage):
	"""Access the System Credential Store from R

	Platform independent 'API' to access the operating system's
    credential store. Currently supports: 'Keychain' on 'macOS',
    Credential Store on 'Windows', the Secret Service 'API' on 'Linux',
    and simple, platform independent stores implemented with environment
    variables or encrypted files.  Additional storage back-ends can be
    added easily.
	"""
	
	homepage = "https://keyring.r-lib.org/"
	cran = "keyring" 

	version("1.3.2", md5="84a59fe23ad0224920a6dd0c7ccda9d0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
