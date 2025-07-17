# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCftools(RPackage):
    """Informatics Tools for Cell-Free DNA Study

    The cfTools R package provides methods for cell-free DNA (cfDNA) methylation data analysis to facilitate cfDNA-based studies. Given the methylation sequencing data of a cfDNA sample, for each cancer marker or tissue marker, we deconvolve the tumor-derived or tissue-specific reads from all reads falling in the marker region. Our read-based deconvolution algorithm exploits the pervasiveness of DNA methylation for signal enhancement, therefore can sensitively identify a trace amount of tumor-specific or tissue-specific cfDNA in plasma. cfTools provides functions for (1) cancer detection: sensitively detect tumor-derived cfDNA and estimate the tumor-derived cfDNA fraction (tumor burden); (2) tissue deconvolution: infer the tissue type composition and the cfDNA fraction of multiple tissue types for a plasma cfDNA sample. These functions can serve as foundations for more advanced cfDNA-based studies, including cancer diagnosis and disease monitoring.
    """

    homepage = "https://github.com/jasminezhoulab/cfTools"
    bioc = "cfTools"

    version("1.8.0", commit="c1e77351ce88a1cd81b93953995a8ea9582c4dbd")
    version("1.2.0", commit="c33a0cc4da4a29cdb1e130ef447483712f10cc58")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-cftoolsdata", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
