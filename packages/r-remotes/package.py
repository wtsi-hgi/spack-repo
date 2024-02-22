# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemotes(RPackage):
	"""R Package Installation from Remote Repositories, Including 'GitHub'.

	Download and install R packages stored in 'GitHub', 'BitBucket', or plain
	'subversion' or 'git' repositories. This package provides the 'install_*'
	functions in 'devtools'. Indeed most of the code was copied over from
	'devtools'."""

	cran = "remotes"

	version("2.4.2.1", md5="65b224c78cbc0a1d80499af5a5152f58")

	depends_on("r@3:", type=("build", "run"))
