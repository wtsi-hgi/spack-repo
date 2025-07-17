# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiffustats(RPackage):
    """Diffusion scores on biological networks

    Label propagation approaches are a widely used procedure in computational biology for giving context to molecular entities using network data. Node labels, which can derive from gene expression, genome-wide association studies, protein domains or metabolomics profiling, are propagated to their neighbours in the network, effectively smoothing the scores through prior annotated knowledge and prioritising novel candidates. The R package diffuStats contains a collection of diffusion kernels and scoring approaches that facilitates their computation, characterisation and benchmarking.
    """

    bioc = "diffuStats"

    version("1.28.0", commit="1337c07352c626a1674b9d550d1c61f9fddf42b7")
    version("1.22.0", commit="9c35facdd538c1049f49e505a808f93ab7f026ac")

    depends_on("r@3.4:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-expm", type=("build", "run"))
    depends_on("r-igraph", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-rcppparallel", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-precrec", type=("build", "run"))
