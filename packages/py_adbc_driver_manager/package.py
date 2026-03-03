# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdbcDriverManager(PythonPackage):
    """This package contains bindings for the ADBC Driver Manager, as well as a DBAPI 2.0/PEP 249-compatible interface on top. This can be used to load ADBC drivers at runtime and use them from Python. Backend-specific packages like adbc_driver_postgresql wrap this package in a more convenient interface, and should be preferred where they exist."""

    homepage = "https://arrow.apache.org/adbc/current/index.html"
    url = "https://files.pythonhosted.org/packages/54/57/6ca02e1584ade06ce7db01de886a38eac9850765796ed7e357dca1d93f85/adbc_driver_manager-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

    version("0.9.0-py312", sha256="70b4cecbf4196fe06e6f8d6bcaddbff56f8e8dfd95b3443c2640de7d9c19d2f0", expand=False, url="https://files.pythonhosted.org/packages/54/57/6ca02e1584ade06ce7db01de886a38eac9850765796ed7e357dca1d93f85/adbc_driver_manager-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.9.0-py311", sha256="4f38e098b0d02d03e6c1c612167ad2e589141f6ee6c513ef1321edac90bf66f2", expand=False, url="https://files.pythonhosted.org/packages/20/e0/e78ec304d3f9eb57547c506be1a6301ddfa99d2d9499005fc7762287c9f9/adbc_driver_manager-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.9.0-py310", sha256="7adca37f8e4a0bb164c3c43b603013f85df30a75bbdf3329c15fa4ae463736c0", expand=False, url="https://files.pythonhosted.org/packages/36/fe/63286e9d16965b60aa9af0d271aa10398fbfdb6204b4ce05ea102927521a/adbc_driver_manager-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")
    version("0.9.0-py309", sha256="3ab7cd84d2dc5574eae03d0e8f713b3eb75c929cb01fae80bf877ee06cc3ef86", expand=False, url="https://files.pythonhosted.org/packages/d3/f3/4b7d957be78b8aac9c66e6edb06b272bafeffff94cbafd4681f3972a4294/adbc_driver_manager-0.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl")

    depends_on("python@3.12", when="@0.9.0-py312")
    depends_on("python@3.11", when="@0.9.0-py311")
    depends_on("python@3.10", when="@0.9.0-py310")
    depends_on("python@3.9", when="@0.9.0-py309")
