# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cairomm(MesonPackage):
    """Cairomm is a C++ wrapper for the cairo graphics library."""

    homepage = "https://www.cairographics.org/cairomm/"
    url = "https://cairographics.org/releases/cairomm-1.16.2.tar.xz"

    license("LGPL-2.0-or-later AND MPL-1.1")

    version("1.18.0", sha256="b81255394e3ea8e8aa887276d22afa8985fc8daef60692eb2407d23049f03cfb")
    version("1.17.1", sha256="343e8463ff7dd4d2c90991d6284a2203431e711026575207fd4c313cd323fdbe")
    version("1.16.2", sha256="6a63bf98a97dda2b0f55e34d1b5f3fb909ef8b70f9b8d382cb1ff3978e7dc13f")
    version("1.16.1", sha256="6f6060d8e98dd4b8acfee2295fddbdd38cf487c07c26aad8d1a83bb9bff4a2c6")
    version("1.16.0", sha256="7e881492c5f9f546688c31160deb742c166fc4c68b6b8eb9920c00a0f0f144f9")
    version("1.14.5", sha256="70136203540c884e89ce1c9edfb6369b9953937f6cd596d97c78c9758a5d48db")
    version("1.14.4", sha256="4749d25a2b2ef67cc0c014caaf5c87fa46792fc4b3ede186fb0fc932d2055158")
    version("1.14.3", sha256="0d37e067c5c4ca7808b7ceddabfe1932c5bd2a750ad64fb321e1213536297e78")
    version("1.14.2", sha256="0126b9cc295dc36bc9c0860d5b720cb5469fd78d5620c8f10cc5f0c07b928de3")
    version("1.14.0", sha256="b64400a78304b2fba13036130d78ebf7588675546714fd5329d97ec80ed01217")

    depends_on("cairo")
    # sigcpp gives sigc++-3.0 and linsigcpp gives sigc++-2.0
    depends_on("sigcpp", type=("build", "run", "link"), when="@1.16:")
    depends_on("libsigcpp", type=("build", "run", "link"), when="@:1.14")
    depends_on("cmake", type="build")
