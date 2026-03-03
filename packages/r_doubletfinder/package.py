from spack.package import *


class RDoubletfinder(RPackage):
    """DoubletFinder: Identify doublets in single-cell RNA-seq data.

    DoubletFinder identifies doublets by generating artificial doublets from
    existing scRNA-seq data and defining which real cells preferentially
    co-localize with artificial doublets in gene expression space.
    """

    homepage = "https://github.com/chris-mcginnis-ucsf/DoubletFinder"
    git = "https://github.com/chris-mcginnis-ucsf/DoubletFinder.git"

    # Latest commit as of recipe creation
    version("20250321", commit="1b244d8f0d54b4b1cb4365639931bbb16f01e1cd")
    version("2023.-08-18", commit="1b1d4e2d7f893a3552d9f8f791ab868ee4c782e6")

    license("CC0-1.0")

    depends_on("r@4.0.0:", type=("build", "run"))

    # Optional suggests
    variant("testthat", default=False, description="Enable testthat suggested dependency")
    depends_on("r-testthat", when="+testthat", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-fields")
        depends_on("r-kernsmooth")
        depends_on("r-rocr")
        depends_on("r-seurat")
        depends_on("r-seuratobject")

