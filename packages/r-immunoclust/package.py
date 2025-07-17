# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImmunoclust(RPackage):
    """immunoClust - Automated Pipeline for Population Detection in Flow Cytometry

    immunoClust is a model based clustering approach for Flow Cytometry samples. The cell-events of single Flow Cytometry samples are modelled by a mixture of multinominal normal- or t-distributions. The cell-event clusters of several samples are modelled by a mixture of multinominal normal-distributions aiming stable co-clusters across these samples.
    """

    bioc = "immunoClust"

    version("1.40.0", commit="c20d14fe8c95c248beda7effb19ca0cf8e269714")
    version("1.34.0", commit="6c8b7f4f36fa7306e784e117c217c1c48bf8276e")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("gsl", type=("build", "link", "run"))
