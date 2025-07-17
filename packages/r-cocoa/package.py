# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocoa(RPackage):
    """Coordinate Covariation Analysis

    COCOA is a method for understanding epigenetic variation among samples. COCOA can be used with epigenetic data that includes genomic coordinates and an epigenetic signal, such as DNA methylation and chromatin accessibility data. To describe the method on a high level, COCOA quantifies inter-sample variation with either a supervised or unsupervised technique then uses a database of "region sets" to annotate the variation among samples. A region set is a set of genomic regions that share a biological annotation, for instance transcription factor (TF) binding regions, histone modification regions, or open chromatin regions. COCOA can identify region sets that are associated with epigenetic variation between samples and increase understanding of variation in your data.
    """

    homepage = "http://code.databio.org/COCOA/"
    bioc = "COCOA"

    version("2.22.0", commit="15583ed526d4f63e254c044fc4d13001f5122273")
    version("2.16.0", commit="d18f2bc0c41476e3daf7f5a7de55012bdec20233")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-complexheatmap", type=("build", "run"))
    depends_on("r-mira", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-simplecache", type=("build", "run"))
    depends_on("r-fitdistrplus", type=("build", "run"))
