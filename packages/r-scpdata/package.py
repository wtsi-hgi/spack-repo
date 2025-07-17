# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScpdata(RPackage):
    """Single-Cell Proteomics Data Package

    The package disseminates mass spectrometry (MS)-based single-cell proteomics (SCP) datasets. The data were collected from published work and formatted using the `scp` data structure. The data sets contain quantitative information at spectrum, peptide and/or protein level for single cells or minute sample amounts.
    """

    bioc = "scpdata"

    version("1.16.1", commit="229186a3fdd7aeeb4f2476940a2667abeb261947")
    version("1.10.0", commit="5495c420fc0273ff006e964b1e3f41be9b2530b4")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-qfeatures", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
