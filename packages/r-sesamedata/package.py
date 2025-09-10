# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSesamedata(RPackage):
    """Supporting Data for SeSAMe Package

    Provides supporting annotation and test data for SeSAMe package. This includes chip tango addresses, mapping information, performance annotation, and trained predictor for Infinium array data. This package provides user access to essential annotation data for working with many generations of the Infinium DNA methylation array. Current we support human array (HM27, HM450, EPIC), mouse array (MM285) and the HorvathMethylChip40 (Mammal40) array.
    """

    bioc = "sesameData"

    version("1.26.0", commit="e4c750cb34eef5779fb62b09cadb4260ba944ecc")
    version("1.20.0", commit="ff46e9d52373588a354043bc4a9427b582809884")

    # Align with Bioconductor 3.21 which needs R >= 4.5
    # depends_on("r@4.5:", type=("build", "run"), when="@1.26:")
    depends_on("r@4.2:", type=("build", "run"), when="@:1.25")
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
