# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProteomm(RPackage):
    """Multi-Dataset Model-based Differential Expression Proteomics Analysis Platform

    ProteoMM is a statistical method to perform model-based peptide-level differential expression analysis of single or multiple datasets. For multiple datasets ProteoMM produces a single fold change and p-value for each protein across multiple datasets. ProteoMM provides functionality for normalization, missing value imputation and differential expression. Model-based peptide-level imputation and differential expression analysis component of package follows the analysis described in “A statistical framework for protein quantitation in bottom-up MS based proteomics" (Karpievitch et al. Bioinformatics 2009). EigenMS normalisation is implemented as described in "Normalization of peak intensities in bottom-up MS-based proteomics using singular value decomposition." (Karpievitch et al. Bioinformatics 2009).
    """

    bioc = "ProteoMM"

    version("1.26.0", commit="1dc9f344a355a00f8d633a37c142e941baf322b1")
    version("1.20.0", commit="bdc161706058bfa9891464966ef34a9849cb774b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
    depends_on("r-biomart", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
