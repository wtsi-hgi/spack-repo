# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXlsx2csv(PythonPackage):
    """Converts xlsx files to csv format. Handles large XLSX files. Fast and easy to use."""

    homepage = "https://github.com/dilshod/xlsx2csv"
    pypi = "xlsx2csv/xlsx2csv-0.8.2.tar.gz"

    version("0.8.2", sha256="cdd272c82f8b32f1cee76aeaef87b2ee3549661fddf90f7ecf2310967a16fc84")
