# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeltalake(PythonPackage):
    """Native Delta Lake Python binding based on delta-rs with Pandas integration."""

    homepage = "https://github.com/delta-io/delta-rs"
    pypi = "deltalake/deltalake-0.15.3.tar.gz"

    version("0.15.3", sha256="c24ad4644b92d65dccf132b48c73e61bc07416b7a8b69e345c7f437217c44b2b")

    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-maturin", type=("build"))

    def patch(self):
        filter_file("[profile.test]", "", "Cargo.toml", string=True)
        filter_file("debug = \"line-tables-only\"", "", "Cargo.toml", string=True)
