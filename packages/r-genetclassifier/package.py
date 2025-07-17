# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenetclassifier(RPackage):
    """Classify diseases and build associated gene networks using gene expression profiles

    Comprehensive package to automatically train and validate a multi-class SVM classifier based on gene expression data. Provides transparent selection of gene markers, their coexpression networks, and an interface to query the classifier.
    """

    homepage = "http://www.cicancer.org"
    bioc = "geNetClassifier"

    version("1.48.0", commit="6be36adc65da48bbc24988945c8add11c2e62f70")
    version("1.42.0", commit="d1bee039ff821a1f61bcaf3d0d5c80f23d850aa2")

    depends_on("r@2.10.1:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-ebarrays", type=("build", "run"))
    depends_on("r-minet", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
