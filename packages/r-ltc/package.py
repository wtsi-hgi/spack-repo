from spack.package import *


class RLtc(RPackage):
    """Collection of artistic and nature-inspired color palettes."""

    homepage = "https://github.com/loukesio/ltc-color-palettes"
    url = "https://github.com/loukesio/ltc-color-palettes/archive/refs/tags/v0.4.0.tar.gz"
    git = "https://github.com/loukesio/ltc-color-palettes.git"

    license("MIT")

    version("0.4.0", sha256="beb66d2e274699ece354a7c8fbb7712871fbbc56a1f33a7508300b25d366e30f")

    depends_on("r", type=("build", "run"))
    depends_on("r-colorspace", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
