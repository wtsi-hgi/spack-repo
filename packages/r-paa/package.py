# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPaa(RPackage):
    """PAA (Protein Array Analyzer)

    PAA imports single color (protein) microarray data that has been saved in gpr file format - esp. ProtoArray data. After preprocessing (background correction, batch filtering, normalization) univariate feature preselection is performed (e.g., using the "minimum M statistic" approach - hereinafter referred to as "mMs"). Subsequently, a multivariate feature selection is conducted to discover biomarker candidates. Therefore, either a frequency-based backwards elimination aproach or ensemble feature selection can be used. PAA provides a complete toolbox of analysis tools including several different plots for results examination and evaluation.
    """

    homepage = "http://www.ruhr-uni-bochum.de/mpc/software/PAA/"
    bioc = "PAA"

    version("1.42.0", commit="0f1a222db3d4baf8f6752299dd525657b038f1e4")
    version("1.36.0", commit="a526b6a2be5871d0591e6d15241cebc5890293c1")

    depends_on("r@3.2:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-mrmre", type=("build", "run"))
    depends_on("r-randomforest", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
