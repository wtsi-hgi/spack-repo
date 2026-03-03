# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyArro3Core(PythonPackage):
    """Core library for representing Arrow data in Python."""

    homepage = "https://kylebarron.dev/arro3"
    pypi = "arro3-core/arro3_core-0.4.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

    version("0.4.1", sha256="8a68f6e5de66ad01a59c86f98382efd69704e50a4492b26278a262b72872add5", expand=False)

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10", type=("build", "run"))
    depends_on("py-maturin", type="build")
