# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyDuckdb(PythonPackage):
    """DuckDB Python package."""

    homepage = "https://github.com/duckdb/duckdb-python"

    version(
        "2.0.0",
        sha256="09de511ef0dc76a5213e8d3d87a8b89bb4d3e8a6fe73a9f60dc001269946b44f",
        url="https://files.pythonhosted.org/packages/c2/7c/dfdf5e9cebefd032f57f09b224993e861ecb55f61e36c709544b04b44f70/duckdb-2.0.0.tar.gz"
    )
    version(
        "1.5.6",
        sha256="166a91dbfacfc0c9f08cc76c0243cb6d3d4296bfab5bad72a3cfb63140a5b7c8",
        url="https://files.pythonhosted.org/packages/59/0b/d65ea3be00ea79aa276a8388bec588a9cbf409ce637c6d306e5316210d15/duckdb-1.5.6.tar.gz",
    )
    version(
        "1.2.2",
        sha256="1e53555dece49201df08645dbfa4510c86440339889667702f936b7d28d39e43",
        url="https://files.pythonhosted.org/packages/28/b8/0f86278684fb7a1fac7c0c869fc6d68ed005cdc91c963eb4373e0551bc0a/duckdb-1.2.2.tar.gz"
    )


    depends_on("python@3.11:", when="@2:", type=("build", "run"))
    depends_on("python@3.10:", when="@1.5:", type=("build", "run"))
    depends_on("py-setuptools-scm@8:", when="@1.5:1", type="build")

    # 1.2.x sdists use the setuptools backend
    depends_on("py-setuptools@60:", when="@:1.2", type="build")
    depends_on("py-setuptools-scm@6.4:", when="@:1.2", type="build")

    depends_on("py-scikit-build-core@0.11.4:", when="@1.5:", type="build")
    depends_on("cmake@3.29:", when="@1.5:", type="build")
    depends_on("ninja@1.10:", when="@1.5:", type="build")
    depends_on("py-nanobind@3:", when="@2:", type="build")
    depends_on("py-numpy@1.19:", when="@2:", type=("build", "run"))
    depends_on("py-pybind11@2.6:", when="@:1", type="build")


    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import duckdb")
