from spack.package import *


class RPolars(RPackage):
    """R bindings for the Polars Rust library."""

    homepage = "https://pola-rs.github.io/r-polars/"
    url = "https://github.com/pola-rs/r-polars/archive/refs/tags/v1.13.0.tar.gz"
    git = "https://github.com/pola-rs/r-polars.git"

    license("MIT")

    version("1.13.0", sha256="112901bc890b299b3d6325576f6e6e2497c07358ee2eab2884193b1baf132a96")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-rlang@1.2.0:", type=("build", "run"))
    depends_on("r-s7@0.2.1:", type=("build", "run"))
    depends_on("rust", type=("build", "link", "run"))

