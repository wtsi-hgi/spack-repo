# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandoc(PythonPackage):
    """Pandoc is the awesome open-source command-line tool that converts documents from one format to another. The project was initiated by John MacFarlane; under the hood, it's a Haskell library."""

    homepage = "https://github.com/boisgera/pandoc"
    pypi = "pandoc/pandoc-2.3.tar.gz"

    version("2.3", sha256="e772c2c6d871146894579828dbaf1efd538eb64fc7e71d4a6b3a11a18baef90d")

    depends_on("py-plumbum", type=("build", "run"))
    depends_on("py-ply", type=("build", "run"))
