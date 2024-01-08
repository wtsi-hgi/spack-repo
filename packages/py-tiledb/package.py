# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTiledb(PythonPackage):
    """Pythonic interface to the TileDB array storage manager."""

    homepage = "https://github.com/TileDB-Inc/TileDB-Py"
    pypi = "tiledb/tiledb-0.23.1.tar.gz"

    version("0.24.0", sha256="6e1f2f0391d5f5d76ae832da6add17d38d9c506b7105fe19823628b5ddb39af6")
    version("0.23.1", sha256="988be85a558510aea5487a1cf981b180974ded93517f6859e262b9ea26257c81")

    depends_on("py-setuptools@42:")
    depends_on("py-pybind11@:2.10.4")
    depends_on("py-cython@:0.29.36")
    depends_on("py-wheel")
    depends_on("cmake")
    depends_on("py-numpy")
    depends_on("zip", when="@0.24.0:")
    depends_on("pkgconfig", when="@0.24.0:")
    depends_on("bzip2", when="@0.24.0:")
