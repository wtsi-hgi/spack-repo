# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install duckdb
#
# You can edit this file again by typing:
#
#     spack edit duckdb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyDuckdb(PythonPackage):
    """DuckDB Python package."""

    homepage = "https://github.com/duckdb/duckdb/tree/main/tools/pythonpkg"
    url = "https://files.pythonhosted.org/packages/28/b8/0f86278684fb7a1fac7c0c869fc6d68ed005cdc91c963eb4373e0551bc0a/duckdb-1.2.2.tar.gz"

    version("1.2.2", sha256="1e53555dece49201df08645dbfa4510c86440339889667702f936b7d28d39e43")

    depends_on("duckdb")
    depends_on("py-setuptools")
    depends_on("py-pybind11")
