from spack.package import *


class RDaesc(RPackage):
    """Differential Allelic Expression using Single-Cell data.

    DAESC performs differential allele-specific expression (ASE) analysis
    using single-cell RNA-seq data across multiple individuals. It supports
    comparisons represented by a design matrix, including discrete cell types,
    continuous cell states (e.g., pseudotime), case-control status, and
    continuous donor phenotypes.
    """

    homepage = "https://github.com/gqi/DAESC"
    git = "https://github.com/gqi/DAESC.git"

    license("GPL-2.0")

    # Use full commit hash with commit date as version id
    version("20240628", commit="af260814982775f8c361e53fb738f637f08857c0")

    depends_on("r@4.0:", type=("build", "run"))

    # DESCRIPTION Depends/Imports
    with default_args(type=("build", "run")):
        depends_on("r-data-table")
        depends_on("r-dplyr")
        depends_on("r-lme4")
        depends_on("r-aod")
        depends_on("r-statmod")
        depends_on("r-numderiv")

