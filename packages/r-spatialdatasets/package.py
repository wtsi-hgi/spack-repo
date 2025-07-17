# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdatasets(RPackage):
    """Collection of spatial omics datasets

    This is a collection of publically available spatial omics datasets. Where possible we have curated these datasets as either SpatialExperiments, MoleculeExperiments or CytoImageLists and included annotations of the sample characteristics.
    """

    homepage = "https://github.com/SydneyBioX/SpatialDatasets"
    bioc = "SpatialDatasets"

    version("1.6.3", commit="ea2889c3cf3d3d79b35114dce4f2f1154a18d3f6")
    version("1.0.0", commit="a93a6e3492f5f09e52eab4d27cfde42446fa2396")

    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-spatialexperiment", type=("build", "run"))
