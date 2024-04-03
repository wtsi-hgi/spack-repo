# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilelock(RPackage):
	"""Portable File Locking.

	Place an exclusive or shared lock on a file. It uses 'LockFile' on Windows
	and 'fcntl' locks on Unix-like systems."""

	cran = "filelock"
	version("1.0.2", sha256="ac2915950789b16c43a625a2b8dab6ba423588db4a7d0daa75b74518b82b1403")
	version("1.0.3", md5="db8ce0e4e54049a51875108aa996bbdb")

	depends_on("r@3.4:", type=("build", "run"))
