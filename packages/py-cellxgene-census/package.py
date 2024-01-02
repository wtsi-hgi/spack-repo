# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCellxgeneCensus(PythonPackage):
    """The cellxgene_census package provides an API to facilitate the use of the CZ CELLxGENE Discover Census."""

    homepage = "https://chanzuckerberg.github.io/cellxgene-census/"
    pypi = "cellxgene_census/cellxgene_census-1.6.0.tar.gz"

    version("1.6.0", sha256="bf176601ee159b357a4c0ae233328aa87dd28dbd89be3f4c0710c8961288404d")

    depends_on("py-setuptools", type=("build", "run"))
    depends_on("py-tiledbsoma@1.4.3:", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-numpy@1.21:1.25", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-s3fs@2021.06.1:", type=("build", "run"))
    depends_on("py-scipy@:1.11", type=("build", "run"))
