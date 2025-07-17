# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniprotkeywords(RPackage):
    """Keywords from UniProt Database

    UniProt database provides a list of controlled vocabulary represented as keywords for genes or proteins. This is useful for summarizing gene functions in a compact way. This package provides data of keywords hierarchy and gene-keyword relations.
    """

    homepage = "https://github.com/jokergoo/UniProtKeywords"
    bioc = "UniProtKeywords"

    version("0.99.7", commit="342c7c1a1f28692ae7a11beb98489c6c0cc34e64")
    version("0.99.7", commit="342c7c1a1f28692ae7a11beb98489c6c0cc34e64")

    depends_on("r@4:", type=("build", "run"))
