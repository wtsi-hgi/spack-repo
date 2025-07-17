# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsobar(RPackage):
    """Analysis and quantitation of isobarically tagged MSMS proteomics data

    isobar provides methods for preprocessing, normalization, and report generation for the analysis of quantitative mass spectrometry proteomics data labeled with isobaric tags, such as iTRAQ and TMT. Features modules for integrating and validating PTM-centric datasets (isobar-PTM). More information on http://www.ms-isobar.org.
    """

    homepage = "https://github.com/fbreitwieser/isobar"
    bioc = "isobar"

    version("1.54.0", commit="538264fd5630b6705f1afbd8196eb23bd6493af6")
    version("1.48.0", commit="b67e33aeead47c05fd4cff7f147eeb47cb664d75")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-distr", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
