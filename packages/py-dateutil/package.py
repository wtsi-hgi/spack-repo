# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDateutil(PythonPackage):
    """The dateutil module provides powerful extensions to the standard datetime module, available in Python."""

    homepage = "https://bitbucket.org/cld/dateutil/src/master/"
    pypi = "py-dateutil/py-dateutil-2.2.tar.gz"

    version("2.2", sha256="7efa2ca17159c590408cb624de9aa10d360f14097cb70dd7559e632f2cf4b048")

    depends_on("py-six", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"))
