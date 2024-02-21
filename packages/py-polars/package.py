# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPolars(PythonPackage):
    """Polars is a DataFrame interface on top of an OLAP Query Engine implemented in Rust using Apache Arrow Columnar Format as the memory model."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-0.20.7.tar.gz"

    #version("0.20.10", sha256="ab32a232916df61c9377edcb5893d0b1624d810444d8fa627f9885d33819a8b7") # All of v0.20 is BROKEN
    version("0.19.19", sha256="3e904d197aabf36e37fda263470eaf51ec92fb865cdea4f93947713480199303")


    depends_on("py-maturin", type=("build"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-pydantic@2.0.0:", type=("build", "run"))
    depends_on("py-sqlalchemy", type=("build", "run"))
    depends_on("py-adbc-driver-manager", type=("build", "run"))
    depends_on("py-adbc-driver-sqlite", type=("build", "run"))
    depends_on("py-connectorx", type=("build", "run"))
    depends_on("py-cloudpickle", type=("build", "run"))
    depends_on("py-fsspec", type=("build", "run"))
    depends_on("py-s3fs", type=("build", "run"))
    depends_on("py-ezodf", type=("build", "run"))
    depends_on("py-lxml", type=("build", "run"))
    depends_on("py-fastexcel@0.8.0:", type=("build", "run"))
    depends_on("py-openpyxl", type=("build", "run"))
    depends_on("py-pyxlsb", type=("build", "run"))
    depends_on("py-xlsx2csv", type=("build", "run"))
    depends_on("py-xlsxwriter", type=("build", "run"))
    depends_on("py-deltalake@0.14.0:", type=("build", "run"))
    depends_on("py-pyiceberg@0.5.0:", type=("build", "run"))
    depends_on("py-zstandard", type=("build", "run"))
    depends_on("py-hvplot@0.9.1:", type=("build", "run"))
    depends_on("py-gevent", type=("build", "run"))
    depends_on("cmake", type=("build", "link"))

    def setup_build_environment(self, env):
        env.set("CARGO_NET_GIT_FETCH_WITH_CLI", "true")
