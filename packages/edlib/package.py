# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Edlib(CMakePackage):
    """A lightweight and super fast C/C++ library for sequence alignment using edit distance."""

    homepage = "https://github.com/Martinsos/edlib"
    url = "https://github.com/Martinsos/edlib/archive/refs/tags/v1.2.7.tar.gz"

    version("1.2.7", sha256="8767bc1b04a1a67282d57662e5702c4908996e96b1753b5520921ff189974621")
    version("1.2.6", sha256="0436f14b0339dabd2aab7faf3779ac1b4bbbdc46246c1bff49be997fe4b4e2c7")
    version("1.2.5", sha256="5d2e3b459713cb45ecc071b6a05362cce8748fc7ae36198ffc55156b2b0a1b2c")
    version("1.2.4", sha256="ddc6892a41d7e4bcee048f282738b1522b67252ec276e4d75284b977fa8eb65d")
    version("1.2.3", sha256="c8b2049daeff2717fb24e3e0a161aec9d9e146f37f67ab2cfda60500208399d2")
    version("1.2.1", sha256="ed9de53fb78cff1bd035469819130326bdedd474d44e65d12fc202f05ddf7587")
    version("1.2.0", sha256="83a34c52900f81bd847c2f18d3d07b87751a41cc75dedd5d7ba68e39cc849d9c")
    version("1.1.2", sha256="931cd09c3b47c431fd7b9adfc80b4cd742b1fbbb25218df33b54c2b6296b0b14")
    version("1.1.1", sha256="f363cbc9e74b6a24e16696b9c818a35f07de934f9b2ce9ca78dfeea76a11ab4b")
    version("1.1.0", sha256="2a1e209f602cee40af223a543964a8bba82d1ffeb6390fe83b6762a70d8ec3f1")
