# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastparquet(PythonPackage):
    """fastparquet is a python implementation of the parquet format, aiming integrate into python-based big data work-flows. It is used implicitly by the projects Dask, Pandas and intake-parquet."""

    homepage = "https://github.com/dask/fastparquet/"
    pypi = "fastparquet/fastparquet-2024.2.0.tar.gz"

    version("2024.2.0", sha256="81a8f60c51793eb2436b4fdbbf115ff8578a4a457a179240bc08f9d9573d57a4")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    # depends_on("python@2.X:2.Y,3.Z:", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    depends_on("py-numpy@1.20.3:", type=("build", "run"))
    depends_on("py-pandas@1.5.0:", type=("build", "run"))
    depends_on("py-cython@0.29.23:", type=("build", "run"))
    depends_on("py-cramjam@2.3:", type=("build", "run"))
    depends_on("py-fsspec", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
