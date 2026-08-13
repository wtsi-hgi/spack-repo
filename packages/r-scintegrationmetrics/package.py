from spack.package import *


class RScintegrationmetrics(RPackage):
    """Metrics of integration performance for scRNA-seq data.

    A collection of metrics to evaluate scRNA-seq integration,
    including LISI and silhouette coefficient.
    """

    homepage = "https://github.com/carmonalab/scIntegrationMetrics"
    url = "https://github.com/carmonalab/scIntegrationMetrics/archive/refs/tags/v1.2.0.tar.gz"
    git = "https://github.com/carmonalab/scIntegrationMetrics.git"

    license("GPL-3")

    version("1.2.0", sha256="470415cf826f219b086b4f9b563964be4945cffce39dbc2783b2484e958bf552")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "link", "run"))
    depends_on("r-rcpparmadillo", type=("build", "link", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rann", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
