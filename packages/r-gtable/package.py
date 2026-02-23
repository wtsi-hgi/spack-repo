# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGtable(RPackage):
	"""Arrange 'Grobs' in Tables.

	Tools to make it easier to work with "tables" of 'grobs'. The 'gtable'
	package defines a 'gtable' grob class that specifies a grid along with a
	list of grobs and their placement in the grid. Further the package makes it
	easy to manipulate and combine 'gtable' objects so that complex
	compositions can be build up sequentially."""

	license("MIT")

	cran = "gtable"
	version("0.3.6", sha256="d305a5fa11278b649d2d8edc5288bf28009be888a42be58ff8714018e49de0ef")
	version("0.3.5", sha256="b19fc1a30359945adbab7d4e915fe95523a839c380e34ae705d70b7ebddeea72")
	version("0.3.4", sha256="7032039371a4ec1bde9d3e4b7dae450dcc9aab50bb0e6287ab26a1b0199c7977")
	version("0.3.3", sha256="2f9a58d978e2a487b7fd8841539ea33cf948e55ddf6f7a9bd2dd3362600a7b3a")
	version("0.3.2", sha256="8d478f7dfb4e6dcf80ad0e277b028bd29c565f6666f0aa83f9decfede71626c8")
	version("0.3.1", sha256="8bd62c5722d5188914d667cabab12991c555f657f4f5ce7b547571ae3aec7cb5")
	version("0.3.0", sha256="fd386cc4610b1cc7627dac34dba8367f7efe114b968503027fb2e1265c67d6d3")
	version("0.2.0", sha256="801e4869830ff3da1d38e41f5a2296a54fc10a7419c6ffb108582850c701e76f")
	version("0.1.2", sha256="b08ba8e62e0ce05e7a4c07ba3ffa67719161db62438b04f14343f8928d74304d")
	version("0.1.1", sha256="03a713b5f353353c56ec3178736440b060791f68321d6557cf5be0719b5fb9f4")

	depends_on("r@3.5:", type=("build", "run"), when="@:0.3.5")
	depends_on("r@4:", type=("build", "run"), when="@0.3.6:")
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
