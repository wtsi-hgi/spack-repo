# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsqrob2(RPackage):
    """Robust statistical inference for quantitative LC-MS proteomics

    msqrob2 provides a robust linear mixed model framework for assessing differential abundance in MS-based Quantitative proteomics experiments. Our workflows can start from raw peptide intensities or summarised protein expression values. The model parameter estimates can be stabilized by ridge regression, empirical Bayes variance estimation and robust M-estimation. msqrob2's hurde workflow can handle missing data without having to rely on hard-to-verify imputation assumptions, and, outcompetes state-of-the-art methods with and without imputation for both high and low missingness. It builds on QFeature infrastructure for quantitative mass spectrometry data to store the model results together with the raw data and preprocessed data.
    """

    homepage = "https://github.com/statOmics/msqrob2"
    bioc = "msqrob2"

    version("1.16.0", commit="0477b1b229076ab5adeb218633c52b1dc793e014")
    version("1.10.0", commit="6bf2b78d17f11a3f7c956f5a24fb7747c96a913f")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-qfeatures@1.1.2:", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-multiassayexperiment", type=("build", "run"))
    depends_on("r-codetools", type=("build", "run"))
