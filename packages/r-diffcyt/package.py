# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffcyt(RPackage):
    """Differential discovery in high-dimensional cytometry via high-resolution clustering

    Statistical methods for differential discovery analyses in high-dimensional cytometry data (including flow cytometry, mass cytometry or CyTOF, and oligonucleotide-tagged cytometry), based on a combination of high-resolution clustering and empirical Bayes moderated tests adapted from transcriptomics.
    """

    homepage = "https://github.com/lmweber/diffcyt"
    bioc = "diffcyt"

    version("1.28.0", commit="df8eb940a6701d6356506daf5dce9700b1593bf7")
    version("1.22.1", commit="871da65dced430198dad3ae2f60054429d3b26e5")
    version("1.22.0", md5="8118267e493c2646533a9730a876d340")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-flowsom", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-multcomp", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
