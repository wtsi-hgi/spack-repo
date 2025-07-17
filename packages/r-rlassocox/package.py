# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlassocox(RPackage):
    """A reweighted Lasso-Cox by integrating gene interaction information

    RLassoCox is a package that implements the RLasso-Cox model proposed by Wei Liu. The RLasso-Cox model integrates gene interaction information into the Lasso-Cox model for accurate survival prediction and survival biomarker discovery. It is based on the hypothesis that topologically important genes in the gene interaction network tend to have stable expression changes. The RLasso-Cox model uses random walk to evaluate the topological weight of genes, and then highlights topologically important genes to improve the generalization ability of the Lasso-Cox model. The RLasso-Cox model has the advantage of identifying small gene sets with high prognostic performance on independent datasets, which may play an important role in identifying robust survival biomarkers for various cancer types.
    """

    bioc = "RLassoCox"

    version("1.16.0", commit="b2b4b8f9de5ccb239ecf16b992bab95b278d2157")
    version("1.10.0", commit="9fb04d641f4e10df9396d648f6f665ae5cf80029")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-glmnet", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
