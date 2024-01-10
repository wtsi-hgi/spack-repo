# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDbDtypes(PythonPackage):
    """Pandas Data Types for SQL systems (BigQuery, Spanner)"""

    homepage = "https://github.com/googleapis/python-db-dtypes-pandas"
    pypi = "db-dtypes/db-dtypes-1.1.1.tar.gz"

    version("1.1.1", sha256="ab485c85fef2454f3182427def0b0a3ab179b2871542787d33ba519d62078883")

    depends_on("py-setuptools", type="build")
