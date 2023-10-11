# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RStopwords(RPackage):
    """Provides multiple sources of stopwords, for use in text analysis and natural language processing."""

    homepage = "https://github.com/quanteda/stopwords"
    cran = "stopwords"

    version("2.3", sha256="c5ec1c6ab1bad1786d87d7823d4b63abc94d2fd84ed7d8e985906e96fb6321b2")
    version("2.2", sha256="b66bccc786200c6ec600be8340e2801bbc7ee787fa5c5a15bc201306861706b9")
    version("2.1", sha256="08c77afd24643320735618002ef9a7e2ecea0e7b9f71d6e2994cf623f54357bc")
    version("2.0", sha256="5cca60ce9f44406486e0dca2e36cec2488096c3558b45fc3bd0e7b6d1500af94")
    version("1.0", sha256="9b727a5d827ac8dcfa6329140d294dcf964a06d80132b4ca434330d0ee02b1da")
    version("0.9.0", sha256="f0bb7f2ab34a46c5cd827131a1b52b4ee363acd9d69c9bff407c341e301c1b14")
    version("0.1.0", sha256="0a6de59880b9e67d5549ce59d25314f08feef0870cdc71da4747fb27a6e2c097")

    depends_on("r-isocodes", type=("build", "run"))
    depends_on("r-covr", type=("build", "run"))
    depends_on("r-testthat", type=("build", "run"))
