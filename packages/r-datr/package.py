# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatr(RPackage):
	"""'Dat' Protocol Interface

	Interface with the 'Dat' p2p network protocol <https://datproject.org>. Clone archives from the network, share your own files, and install packages from the network.
	"""
	
	homepage = "https://github.com/libscie/datr"
	cran = "datr" 

	version("0.1.0", md5="d053e41f2cba5ab814f6949aca9e6e85")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
