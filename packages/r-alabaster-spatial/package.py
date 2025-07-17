# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterSpatial(RPackage):
    """Save and Load Spatial 'Omics Data to/from File

    Save SpatialExperiment objects and their images into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
    """

    bioc = "alabaster.spatial"

    version("1.8.0", commit="72f53213c94b6941436833e27cfae37742ded559")
    version("1.2.0", commit="ec0ca0a01d55296916d66b481ffd476676e70fb2")

    depends_on("r-spatialexperiment", type=("build", "run"))
    depends_on("r-alabaster-base", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-alabaster-sce", type=("build", "run"))
