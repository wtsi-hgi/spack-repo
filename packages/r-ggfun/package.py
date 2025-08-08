# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgfun(RPackage):
	"""Miscellaneous Functions for 'ggplot2'.

	Useful functions to edit 'ggplot' object (e.g., setting fonts for theme and
	layers, adding rounded rectangle as background for each of the legends)."""

	cran = "ggfun"
	version("0.2.0", sha256="c5d267d3152771842ac1fdd819ecb442670946b75d10e0b4866e342d441a1711")
	version("0.1.9", sha256="7c3b8ef3b3c84713ca390aae742e119e62c1d73cebfb5b875a55c864a13caca1")
	version("0.1.8", sha256="083f9e668c8d9d24901a41fc8b9e7288b4f21189681783470c909e6958b63f5c")
	version("0.1.7", sha256="be92efb841751aba6cf83a83b80f3446a76b93ee269dcee8af37a7a1e19a85ea")
	version("0.1.6", sha256="6b7a7dcdd400d52581fb084507d03fb7b140ef07605a17ebc8ded5c7de471aa4")
	version("0.1.5", sha256="fe6c01fd68c17497f23f76dfd4e5a6edd79a6e86850b8c5054748f31527b16d3")
	version("0.1.4", sha256="dc741a141bf401224076c13983e3d991a1e7f5c04c908358ba65c6e1d96533c4")
	version("0.0.9", sha256="5c740e9d1e73b77658f41ed65e21492f4e71b12c7c9ff4b9e52ebf5f8f197612")
	version("0.0.8", sha256="9471a12fc7af203a419767b845e6b6c1e63c080370cb8f2dac80187194122273")
	version("0.0.7", sha256="a83b5fb95f61e366f96d6d8e6b04dafff8e885e7c80c913614876b50ebb8e174")
	version("0.0.6", sha256="59989ed260fcc71cd95487cf3493113a2d8a47d273d9a2f3e5e842609620511b")
	version("0.0.5", sha256="b1e340a8932d2cffbbbf6070ce96c9356599e9955a2b6534fcb17e599c575783")
	version("0.0.4", sha256="5926365f9a90baf47320baf48c40f515ef570f9c767484adea5f04219964d21e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-yulab-utils", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
