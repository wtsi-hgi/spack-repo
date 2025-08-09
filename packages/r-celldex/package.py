# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelldex(RPackage):
    """Reference Index for Cell Types

    Provides a collection of reference expression datasets with curated cell type labels, for use in procedures like automated annotation of single-cell data or deconvolution of bulk RNA-seq.
    """

    homepage = "https://github.com/LTLA/celldex"
    bioc = "celldex"

    version("1.18.0", commit="0a661782b975e8cd96f471e46c7a2037cfd3f9a4")
    version("1.12.0", commit="7567a3154fa2e919349032e954f9a0d295f453c5")

    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-gypsum", type=("build", "run"))
    depends_on("r-alabaster-base", type=("build", "run"))
    depends_on("r-alabaster-matrix", type=("build", "run"))
    depends_on("r-alabaster-se", type=("build", "run"))
