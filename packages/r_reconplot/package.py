from spack.package import *


class RReconplot(RPackage):
    """Plot copy-number profiles alongside inter- and intrachromosomal structural
    variants to study complex genomic rearrangements in cancer genomes."""

    homepage = "https://github.com/cortes-ciriano-lab/ReConPlot"
    git = "https://github.com/cortes-ciriano-lab/ReConPlot.git"

    license("GPL-3.0-or-later")

    version("20241218", commit="88bb76011703d7908aaa2e5bdecfe18ba5737db8")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-ggplot2@3.4.0:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
