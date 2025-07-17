# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdp(RPackage):
    """Molecular Degree of Perturbation calculates scores for transcriptome data samples based on their perturbation from controls

    The Molecular Degree of Perturbation webtool quantifies the heterogeneity of samples. It takes a data.frame of omic data that contains at least two classes (control and test) and assigns a score to all samples based on how perturbed they are compared to the controls. It is based on the Molecular Distance to Health (Pankla et al. 2009), and expands on this algorithm by adding the options to calculate the z-score using the modified z-score (using median absolute deviation), change the z-score zeroing threshold, and look at genes that are most perturbed in the test versus control classes.
    """

    homepage = "https://mdp.sysbio.tools/"
    bioc = "mdp"

    version("1.28.0", commit="849eda1b732439a96967e75fd58a3011b33952ce")
    version("1.22.0", commit="3f17080353f06d072688ef523f6a65abc1bfed7a")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
