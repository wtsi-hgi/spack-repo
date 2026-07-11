# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlatbuffers(PythonPackage):
    """FlatBuffers is an efficient cross platform serialization library for games,
    machine learning, and other performance-critical applications."""

    homepage = "https://google.github.io/flatbuffers/"
    pypi = "flatbuffers/flatbuffers-24.12.23.tar.gz"

    # 24.12.23 fixes the invalid license_files pattern in setup.py
    version("24.12.23", sha256="2910b0bc6ae9b6db78dd2b18d0b7a0709ba240fb5585f286a3a2b30785c22dac")
    version("24.3.25", sha256="de2ec5b203f21441716617f38443e0a8ebf3d25bf0d9c0bb0ce68fa00ad546a4")
    version("24.3.7", sha256="0895c22b9a6019ff2f4de2e5e2f7cd15914043e6e7033a94c0c6369422690f22")
    version("23.5.26", sha256="9ea1144cac05ce5d86e2859f431c6cd5e66cd9c78c558317c7955fb8d4c78d89")
    version("1.12", sha256="63bb9a722d5e373701913e226135b28a6f6ac200d5cc7b4d919fa38d73b44610")

    depends_on("py-setuptools", type="build")
    # setuptools 70.0.0 turned the invalid license_files '../LICENSE' pattern
    # in setup.py into a hard InvalidConfigError; older versions only warned
    depends_on("py-setuptools@:69", when="@:24.3.25", type="build")
