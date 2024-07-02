# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyKrbalancing(PythonPackage):
    """A c++ extension for python to balance a matrix using KR method"""

    homepage = "https://github.com/deeptools/Knight-Ruiz-Matrix-balancing-algorithm"
    url = "https://github.com/dilawar/Knight-Ruiz-Matrix-balancing-algorithm/archive/refs/tags/v0.5.0b0.tar.gz"

    version("0.5.0b0", sha256="b53d7cd1e84759b0dde7a6fa277d4ffe9bdbaead65db9a9a06aa2653ff0594ea")

    depends_on("py-setuptools", type="build")
    depends_on("py-conan", type="build")
    depends_on("py-pybind11", type="build")
    depends_on("eigen", type=("build", "run"))
    depends_on("cmake", type="build")

    patch("conan-cmake.patch")
