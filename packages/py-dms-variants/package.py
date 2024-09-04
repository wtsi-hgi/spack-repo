# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyDmsVariants(PythonPackage):
    """dms_variants is a Python package written by the Bloom lab. It can be used to analyze deep mutational scanning of libraries of barcoded variants, and fit global epistasis models."""

    homepage = "https://jbloomlab.github.io/dms_variants/index.html"
    git = "https://github.com/jbloomlab/dms_variants"
    pypi = "dms_variants/dms_variants-1.5.0.tar.gz"

    version("1.5.0", sha256="ac2d1b89e5621dee899205688048edc7649a448af8df7ba7093706c113dcc32a")


    depends_on("py-setuptools", type="build")

    depends_on("py-biopython@1.73:", type=("build", "run"))
    depends_on("py-matplotlib@3.1:", type=("build", "run"))
    depends_on("py-pandas@1.2:", type=("build", "run"))
    depends_on("py-scipy@1.1.0:", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-plotnine", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-binarymap", type=("build", "run"))

    depends_on("py-regex", type=("build", "run"))

    depends_on("py-dmslogo", type=("build", "run"))
