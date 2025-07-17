# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasicstan(RPackage):
    """Stan implementation of BASiCS

    Provides an interface to infer the parameters of BASiCS using the variational inference (ADVI), Markov chain Monte Carlo (NUTS), and maximum a posteriori (BFGS) inference engines in the Stan programming language. BASiCS is a Bayesian hierarchical model that uses an adaptive Metropolis within Gibbs sampling scheme. Alternative inference methods provided by Stan may be preferable in some situations, for example for particularly large data or posterior distributions with difficult geometries.
    """

    homepage = "https://github.com/Alanocallaghan/BASiCStan"
    bioc = "BASiCStan"

    version("1.10.0", commit="3867fd1d39a9b04c40039044c24538665bacc515")
    version("1.4.0", commit="5172b1599d9d23c63a3d7d1793fcff98f9a75c26")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-basics", type=("build", "run"))
    depends_on("r-rstan@2.18.1:", type=("build", "run"))
    depends_on("r-glmgampoi", type=("build", "run"))
    depends_on("r-scran", type=("build", "run"))
    depends_on("r-scuttle", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rcpp@0.12:", type=("build", "run"))
    depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
    depends_on("r-rstantools@2.1.1:", type=("build", "run"))
    depends_on("r-bh@1.66:", type=("build", "run"))
    depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
    depends_on("r-stanheaders@2.18:", type=("build", "run"))
