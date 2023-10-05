# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTiledb(PythonPackage):
    """Pythonic interface to the TileDB array storage manager."""

    homepage = "https://github.com/TileDB-Inc/TileDB-Py"
    pypi = "tiledb/tiledb-0.23.1.tar.gz"

    version("0.23.1", sha256="988be85a558510aea5487a1cf981b180974ded93517f6859e262b9ea26257c81")

    depends_on("py-setuptools")
    depends_on("py-pybind11")
    depends_on("py-cython@:3")
    depends_on("py-wheel")
    depends_on("cmake")
    depends_on("py-numpy")
