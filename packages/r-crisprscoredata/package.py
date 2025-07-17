# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprscoredata(RPackage):
    """Pre-trained models for the crisprScore package

    Provides an interface to access pre-trained models for on-target and off-target gRNA activity prediction algorithms implemented in the crisprScore package. Pre-trained model data are stored in the ExperimentHub database. Users should consider using the crisprScore package directly to use and load the pre-trained models.
    """

    homepage = "https://github.com/crisprVerse/crisprScoreData/issues"
    bioc = "crisprScoreData"

    version("1.12.0", commit="30e364703a709f52c172dab21cc61f2a61780cb2")
    version("1.6.0", commit="2c66064679b3a30f2f45793e63cf4738b9ab8d9c")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
