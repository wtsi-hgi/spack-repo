from spack.package import *


class RClusterr(RPackage):
    """Gaussian Mixture Models, K-Means, Mini-Batch-Kmeans, K-Medoids and Affinity Propagation Clustering."""

    cran = "ClusterR"

    version("1.3.3", sha256="26d7e34fcbb0d611cbcfe5581c664b80eb6f9d87a6c22a446e0a41a90d06b26e")
    version("1.3.2", sha256="d739817a72adcc2d6d2a7500913689462bf7776c1b52102de91f24ef07d541af")

    depends_on("r@3.0:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-gmp", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
