from spack.package import *


class RNichede(RPackage):
    """NicheDE detects context-dependent changes in gene expression in
    spatial transcriptomic data."""

    homepage = "https://kaishumason.github.io/NicheDE/"
    url = "https://api.github.com/repos/kaishumason/NicheDE/tarball/v.0.0.5"
    git = "https://github.com/kaishumason/NicheDE.git"

    version("0.0.5", sha256="e7f361401e89462a44dbed57adfef49eb785d98a26162d888630709d96005042")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-fastdummies", type=("build", "run"))
    depends_on("r-poolr", type=("build", "run"))
    depends_on("r-spatstat-utils", type=("build", "run"))

