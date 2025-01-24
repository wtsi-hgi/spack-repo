# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPolars(PythonPackage):
    """Blazingly fast DataFrame library."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-0.20.5.tar.gz"

    license("MIT")

    version("0.20.31", sha256="00f62dec6bf43a4e2a5db58b99bf0e79699fe761c80ae665868eaea5168f3bbb")

    # pyproject.toml
    depends_on("py-maturin@1.3.2:", type="build")

    # README.md
    depends_on("rust@1.71:", type="build")
    depends_on("cmake", type="build")
