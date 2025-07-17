# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrthosdata(RPackage):
    """Data for the orthos package

    `orthosData` is the companion ExperimentData package to the `orthos` R package for mechanistic studies using differential gene expression experiments. It provides functions for retrieval from ExperimentHub and local caching of the models and datasets used internally in orthos.
    """

    homepage = "https://github.com/fmicompbio/orthosData"
    bioc = "orthosData"

    version("1.6.0", commit="cd17d9792e1fcf229e0bc0313a4fdd2008384295")
    version("1.0.0", commit="b14e691b7048638d3a4e3547d65ac5d677e51233")

    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
