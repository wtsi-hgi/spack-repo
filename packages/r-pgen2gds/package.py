from spack.package import *


class RPgen2gds(RPackage):
    """Format conversion from PLINK2 PGEN to GDS."""

    homepage = "https://github.com/zhengxwen/pgen2gds"
    bioc = "pgen2gds"
    url = "https://bioconductor.statistik.tu-dortmund.de/packages/3.24/bioc/src/contrib/pgen2gds_0.99.3.tar.gz"

    version("0.99.3", sha256="c9230a7c480f695d17dbd655146f62bb123f783bc796fa23b3456868752cf6d0")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-gdsfmt@1.24.0:", type=("build", "link", "run"))
    depends_on("r-seqarray@1.49.6:", type=("build", "run"))
    depends_on("r-pgenlibr", type=("build", "run"))
