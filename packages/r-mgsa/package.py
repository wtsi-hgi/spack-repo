# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgsa(RPackage):
    """Model-based gene set analysis

    Model-based Gene Set Analysis (MGSA) is a Bayesian modeling approach for gene set enrichment. The package mgsa implements MGSA and tools to use MGSA together with the Gene Ontology.
    """

    homepage = "https://github.com/sba1/mgsa-bioc"
    bioc = "mgsa"

    version("1.56.0", commit="d41a5d21c593781b09f7d9d221e46c7971aab06b")
    version("1.50.0", commit="9aaf4281d60ab4fd30142410eb33c1c0b027bd36")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
