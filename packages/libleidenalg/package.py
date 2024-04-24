# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Libleidenalg(CMakePackage):
    """This package implements the Leiden algorithm in C++."""

    url = "https://github.com/vtraag/libleidenalg/archive/refs/tags/0.11.1.tar.gz"

    version("0.11.1", sha256="7d7392afd214c584e023cc2f0d0ac375f58575c32f2e49ba85062065f1637c7f")
    version("0.11.0", sha256="e3a766449e0bee137e4a8b2c5506c4bdc00cec246ccf1c93d8e86bbd253bc5c4")
    version("0.10.0", sha256="ae265fb718e2233bfd01e3bc9679d9bed53a182e4cb13dbb12b49e6e92105cc7")

    depends_on("igraph@0.10:", type=("build", "link"))
    depends_on("cmake@3.23:", type=("build", "link"))

    #def cmake_args(self):
    #    return ["-DCMAKE_POSITION_INDEPENDENT_CODE=ON"]
