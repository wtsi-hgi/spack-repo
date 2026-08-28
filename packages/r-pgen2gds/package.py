from spack.package import *


class RPgen2gds(RPackage):
    """Format conversion from PLINK2 PGEN to GDS."""

    homepage = "https://github.com/zhengxwen/pgen2gds"
    bioc = "pgen2gds"
    git = "https://git.bioconductor.org/packages/pgen2gds"

    version("0.99.3", commit="e52625a6d881236eee447f8dba5f4c95da6152b3")

    depends_on("r@4.0:", type=("build", "run"))
    depends_on("r-gdsfmt@1.24.0:", type=("build", "link", "run"))
    depends_on("r-seqarray@1.49.6:", type=("build", "run"))
    depends_on("r-pgenlibr", type=("build", "run"))
