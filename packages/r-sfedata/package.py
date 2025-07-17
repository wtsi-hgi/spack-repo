# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfedata(RPackage):
    """Example SpatialFeatureExperiment datasets

    Example spatial transcriptomics datasets with Simple Feature annotations as SpatialFeatureExperiment objects. Technologies include Visium, slide-seq, Nanostring CoxMX, Vizgen MERFISH, and 10X Xenium. Tissues include mouse skeletal muscle, human melanoma metastasis, human lung, breast cancer, and mouse liver.
    """

    homepage = "https://github.com/pachterlab/SFEData"
    bioc = "SFEData"

    version("1.10.0", commit="dab441ba6e9689522608bbed12ff645933da657d")
    version("1.4.0", commit="8fd09254396193597f0c30a9a4d8993428be7889")

    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
