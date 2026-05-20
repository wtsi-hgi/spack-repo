# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythonLevenshtein(PythonPackage):
    """Python extension for computing string edit distances and
    similarities."""

    homepage = "https://github.com/ztane/python-Levenshtein"
    pypi = "python-Levenshtein/python-Levenshtein-0.12.0.tar.gz"

    version("0.27.3", sha256="27dc2d65aeb62a7d6852388f197073296370779286c0860b087357f3b8129a62", url="https://files.pythonhosted.org/packages/f6/b4/36eda4188dd19d3cb53d8a8749d7520bd23dfe1c1f44e56ea9dcd0232274/python_levenshtein-0.27.3.tar.gz")
    version("0.12.0", sha256="033a11de5e3d19ea25c9302d11224e1a1898fe5abd23c61c7c360c25195e3eb1")

    depends_on("py-setuptools", type="build")
