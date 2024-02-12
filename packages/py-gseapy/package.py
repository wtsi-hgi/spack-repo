# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGseapy(PythonPackage):
    """GSEApy: Gene Set Enrichment Analysis in Python."""

    homepage = "https://github.com/zqfang/GSEApy/"
    pypi = "gseapy/gseapy-1.1.1.tar.gz"

    version("1.1.1", sha256="5062fc8d625037beb3d41762cb0cd7cad25653bb3a0c71b8f188ba458da77d4a")

    depends_on("rust", type="build")
    depends_on("py-numpy@1.9.0:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib@1.4.3:", type=("build", "run"))
    depends_on("py-pandas@0.16:", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
