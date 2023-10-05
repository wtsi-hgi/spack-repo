# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTiledbsoma(PythonPackage):
    """Python API for efficient storage and retrieval of single-cell data using TileDB."""

    homepage = "https://github.com/single-cell-data/TileDB-SOMA/tree/main/apis/python"
    pypi = "tiledbsoma/tiledbsoma-1.4.3.tar.gz"

    version("1.4.3", sha256="4f137efd06281b90e673526d55cd4ac2141c3f3f782735b1084fc3fd6b2c2bc5")

    depends_on("py-wheel@0.37.1:", type="build")
    depends_on("py-setuptools@65.5.1:", type=("build", "run"))
    depends_on("cmake@3.21:", type="build")
    depends_on("py-typeguard@:3.0", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-tiledb", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))

