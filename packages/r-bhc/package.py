# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhc(RPackage):
    """Bayesian Hierarchical Clustering

    The method performs bottom-up hierarchical clustering, using a Dirichlet Process (infinite mixture) to model uncertainty in the data and Bayesian model selection to decide at each step which clusters to merge.  This avoids several limitations of traditional methods, for example how many clusters there should be and how to choose a principled distance metric.  This implementation accepts multinomial (i.e. discrete, with 2+ categories) or time-series data. This version also includes a randomised algorithm which is more efficient for larger data sets.
    """

    bioc = "BHC"

    version("1.54.0", commit="79f82ca691e019fd4a2cdd8f5db5584c9b611821")
