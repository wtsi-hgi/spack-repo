# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdbcDriverSqlite(PythonPackage):
    """This package contains bindings for the ADBC SQLite driver, using the driver manager to provide a DBAPI 2.0/PEP 249-compatible interface on top.."""

    homepage = "https://arrow.apache.org/adbc/"
    url = "https://files.pythonhosted.org/packages/47/8b/0e66b80df00f152e9a9255b2185ee0691766ada78e2b2cc4b8d358b09b34/adbc_driver_sqlite-0.9.0-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"

    version("0.9.0", sha256="905de41658f7567f0919e5aa34d1e3261f8a802212c46f06a6b767ba7f07277e", expand=False)
