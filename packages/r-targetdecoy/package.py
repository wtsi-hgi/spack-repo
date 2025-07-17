# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetdecoy(RPackage):
    """Diagnostic Plots to Evaluate the Target Decoy Approach

    A first step in the data analysis of Mass Spectrometry (MS) based proteomics data is to identify peptides and proteins. With this respect the huge number of experimental mass spectra typically have to be assigned to theoretical peptides derived from a sequence database. Search engines are used for this purpose. These tools compare each of the observed spectra to all candidate theoretical spectra derived from the sequence data base and calculate a score for each comparison. The observed spectrum is then assigned to the theoretical peptide with the best score, which is also referred to as the peptide to spectrum match (PSM). It is of course crucial for the downstream analysis to evaluate the quality of these matches. Therefore False Discovery Rate (FDR) control is used to return a reliable list PSMs. The FDR, however, requires a good characterisation of the score distribution of PSMs that are matched to the wrong peptide (bad target hits). In proteomics, the target decoy approach (TDA) is typically used for this purpose. The TDA method matches the spectra to a database of real (targets) and nonsense peptides (decoys). A popular approach to generate these decoys is to reverse the target database. Hence, all the PSMs that match to a decoy are known to be bad hits and the distribution of their scores are used to estimate the distribution of the bad scoring target PSMs. A crucial assumption of the TDA is that the decoy PSM hits have similar properties as bad target hits so that the decoy PSM scores are a good simulation of the target PSM scores. Users, however, typically do not evaluate these assumptions. To this end we developed TargetDecoy to generate diagnostic plots to evaluate the quality of the target decoy method.
    """

    homepage = "https://www.bioconductor.org/packages/TargetDecoy"
    bioc = "TargetDecoy"

    version("1.14.0", commit="1834960b071df999c80a33d4e46a3b7978c92eaf")
    version("1.8.0", commit="bfb3135b874caa8d88338b9f3d4652bf81ca8ee7")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-miniui", type=("build", "run"))
    depends_on("r-mzid", type=("build", "run"))
    depends_on("r-mzr", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
