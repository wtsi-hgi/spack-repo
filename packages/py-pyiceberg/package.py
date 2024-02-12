# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyiceberg(PythonPackage):
    """PyIceberg is a Python implementation for accessing Iceberg tables, without the need of a JVM."""

    homepage = "https://py.iceberg.apache.org/"
    pypi = "pyiceberg/pyiceberg-0.5.1.tar.gz"

    version("0.5.1", sha256="d9e8d1badb576472bd10ccad3ccfdd193027a1892c493e6bb04ed61d8fb57458")

    depends_on("py-poetry-core", type="build")

    depends_on("py-mmhash3@3.0.0:4.0.0", type=("build", "run"))
    depends_on("py-requests@2.20.0:3.0.0", type=("build", "run"))
    depends_on("py-click@7.1.1:9.0.0", type=("build", "run"))
    depends_on("py-rich@10.11.0:14.0.0", type=("build", "run"))
    depends_on("py-strictyaml@1.7.0:2.0.0", type=("build", "run"))
    depends_on("py-pydantic@2.0:3.0", type=("build", "run"))
    depends_on("py-sortedcontainers@2.4.0:", type=("build", "run"))
    depends_on("py-fsspec@2023.1.0:2024.1.0", type=("build", "run"))
    depends_on("py-pyparsing@3.1.0:4.0.0", type=("build", "run"))
    depends_on("py-zstandard@0.13.0:1.0.0", type=("build", "run"))
