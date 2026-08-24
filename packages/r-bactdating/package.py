# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RBactdating(RPackage):
    """Bayesian inference of ancestral dates on bacterial phylogenetic trees"""

    homepage = "https://xavierdidelot.github.io/BactDating/"
    git = "https://github.com/xavierdidelot/BactDating.git"

    license("MIT")

    version("1.1.4", commit="048afb7ebc8550710aae6d861fe148252b984601")
    version("1.1", commit="b878d6b62a23b969d685cafd5ba54b8d2f66a076")
    version("1.0", commit="0156d6f931b3cd0d3f2a656a70018d8556fcb240")

    depends_on("r@3:")
    depends_on("r-rcpp@0.12.13:")
    depends_on("r-ape")


