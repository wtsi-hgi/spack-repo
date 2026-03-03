# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHgicommon(PythonPackage):
    """Common Python used in HGI projects."""

    homepage = "https://github.com/wtsi-hgi/python-common"
    pypi = "hgicommon/hgicommon-1.2.0.tar.gz"
    
    version("1.3.2", sha256="b1c136af067508e700460412da510f725f36e50b28d3170f0c3d4fe308ea21fe")
    version("1.3.1", sha256="89a5a55160e6519d281d5bc2ba7510b47b08713ebf0a8116d545bf9dffdb7cc3")
    version("1.2.0", sha256="1bfcfe47849beaab3a4890ba0bbc29fb6de853b34a4ad09e91b365c61db6308f")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-watchdog@0.8.3:", type=("build", "run"))
    depends_on("py-docker@2.0.1:", type=("build", "run"))

    def patch(self):
        filter_file("Iterable(Any)", "Iterable[Any]", "hgicommon/collections.py", string=True)
