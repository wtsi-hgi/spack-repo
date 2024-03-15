# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RRzmq(RPackage):
	"""R Bindings for 'ZeroMQ'.

	Interface to the 'ZeroMQ' lightweight messaging kernel (see
	<http://www.zeromq.org/> for more information)."""

	cran = "rzmq"

	license("GPL-3.0-only")

	version("0.9.12", md5="516081023e9943a7ed2a5bd104cd82b3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("libzmq@3.0.0:", type=("build", "link", "run"))
