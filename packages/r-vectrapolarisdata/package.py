# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVectrapolarisdata(RPackage):
    """Vectra Polaris and Vectra 3 multiplex single-cell imaging data

    Provides two multiplex imaging datasets collected on Vectra instruments at the University of Colorado Anschutz Medical Campus. Data are provided as a Spatial Experiment objects. Data is provided in tabular form and has been segmented and phenotyped using Inform software. Raw .tiff files are not included.
    """

    homepage = "https://github.com/julia-wrobel/VectraPolarisData"
    bioc = "VectraPolarisData"

    version("1.12.0", commit="a0fd37f4e56fbe28b09287cbee8b9b25530a1cb4")
    version("1.6.0", commit="9848b9be87c999cb89a549303ed4ab83f29a3632")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
