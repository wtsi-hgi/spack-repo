# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *

class Igraph(CMakePackage):
    """igraph is a library for creating and manipulating graphs."""

    homepage = "https://igraph.org/"
    url = "https://github.com/igraph/igraph/releases/download/0.10.7/igraph-0.10.7.tar.gz"

    version("0.10.7", sha256="b9e2a46b70896a379d784ea227f076b59750cc7411463b1d4accbf9e38b361ad")
    version("0.10.6", sha256="99bf91ee90febeeb9a201f3e0c1d323c09214f0b5f37a4290dc3b63f52839d6d")
    version("0.10.5", sha256="1c2725122fda9b72065095794bc7748939d90d942d312cb63c6160cd98d50f1e")
    version("0.10.4", sha256="aa5700b58c5f1e1de1f4637ab14df15c6b20e25e51d0f5a260921818e8f02afc")
    version("0.10.3", sha256="5f72398c7847bb167f85159b7a9fe1fe69ce0f241c5de5d30b2b347f9dc3f7c6")
    version("0.10.2", sha256="2c2b9f18fc2f84b327f1146466942eb3e3d2ff09b6738504efb9e5edf2728c83")
    version("0.10.1", sha256="11ac87336b7adc61b4cb3d9c29fd9ed74db383a1fd994f6c47a870a86f68038c")
    version("0.10.0-rc.2", sha256="f49a555467a7c71cc4c1f5a6babf4ebacc683ffdac00260271f65b045a875f39")
    version("0.10.0", sha256="62e3c9e51ac5b0f1871142aac23956f3a6a337fee980bf5474bd4ac3d76e1a68")
    version("0.9.10", sha256="3e10eb2e0588bf6a2e1e730fb1a685f7591cbe589326f4ac1f5bb45b36664dbe")

    depends_on("libxml2")

    def cmake_args(self):
        return ["-DCMAKE_POSITION_INDEPENDENT_CODE=ON"]
