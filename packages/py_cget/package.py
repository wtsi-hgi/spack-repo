# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCget(PythonPackage):
	"""Cmake package retrieval"""
	
	homepage = "https://github.com/pfultz2/cget"
	pypi = "cget/cget-0.2.0.tar.gz" 

	version("0.0.6", sha256="e98cfa9d6786be62032b5d0dda2429a170793fca0ba3623a71c3616398e4f6f7")
	version("0.0.7", sha256="7f254eafa8c0354e9fae8a20cee2a78a2c996ccac3f0c202cbc74019b9342d02")
	version("0.0.8", sha256="7db775ba279c5000994fd1db666f7638699def1e996cfd3bced51f5c707b9153")
	version("0.0.9", sha256="85f96d762e314cfb88f054184c0b47222679b414358af05fe7199962f50d68b6")
	version("0.1.0", sha256="a7c7005c815007bde6c1f96a448839b4272bbeb81a7afe55e36dc94ee9a70663")
	version("0.1.1", sha256="0cfa8b66fab27227d63ccbead2a7573603338018da397fa384918439569e41d0")
	version("0.1.2", sha256="b2d5d7016716e14867de9ab87bb06386a0915a8f1768a3fa4217dafae4144aef")
	version("0.1.3", sha256="2b7864896cc75cb242532c9dbd6763558e084291ef108fadee0849fc6f09015f")
	version("0.1.4", sha256="2ca51cf7967c0661404fde22362b669d7b7f7aeae048b192948534d57114be27")
	version("0.1.5", sha256="5e43159492ee6bab3269487c5d23b5379aa0ac6bf7826bef8e7b0323a2e7132d")
	version("0.1.6", sha256="353bdb724c4fe5f180f5bb27eebc9e5c57e45b841eb612e5e22d26224443019b")
	version("0.1.7", sha256="6fd72171a7fe0344ad8867e821c88c0e28d5e052d4e83eb0cc27d9108f801416")
	version("0.1.8", sha256="996d286d615fa7cad0bb9249b0450c6f0f915627d0b2f5592fb5c07ca05d74f4")
	version("0.1.9", sha256="2a7913b601bec615208585eda7e69998a43cc17080d36c2ff2ce8742c9794bf6")
	version("0.2.0", sha256="835009ba6d623a36eee8056975d7cdbeebb0e0091a058b572ed433fb12ae18e8")

	depends_on("py-setuptools", type="build")
