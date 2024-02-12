# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygam(PythonPackage):
    """Generalized Additive Models in Python."""

    homepage = "https://pygam.readthedocs.io"
    pypi = "pygam/pygam-0.9.0.tar.gz"

    version("0.9.0", sha256="dba62285a275cdd15a6adf764f6717b3cd077502f01cf1bcee5ce7cbda221956")

    depends_on("py-poetry-core", type="build")

    depends_on("python@:3.12", type=("build", "run"))
    depends_on("py-numpy@1.24.2:", type=("build", "run"))
    depends_on("py-scipy@1.10.1:", type=("build", "run"))
    depends_on("py-progressbar2@4.2.0:", type=("build", "run"))
