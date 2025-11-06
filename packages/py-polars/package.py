from spack.package import *


class PyPolars(PythonPackage):
    """Polars: Fast DataFrame library for Python. Built on Rust.

    This recipe builds from the PyPI sdist using maturin and requires a
    sufficiently recent Rust toolchain to satisfy upstream crate
    requirements.
    """

    homepage = "https://pola.rs"
    pypi = "polars/polars-1.25.2.tar.gz"

    version("1.25.2", sha256="c6bd9b1b17c86e49bcf8aac44d2238b77e414d7df890afc3924812a5c989a4fe")

    # Python compatibility from upstream project metadata
    depends_on("python@3.8:", type=("build", "run"))

    # Build system: use pip+wheel+maturin with an adequate Rust compiler
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-maturin", type="build")
    # Recent crates (e.g., home@0.5.12) require rustc >=1.88
    # Avoid nightly/master toolchains; require a stable Rust release
    depends_on("rust@1.88:1.99", type="build")

    def patch(self):
        # Upstream enables the "nightly" feature by default, which breaks
        # builds with stable rustc. Remove it so we build with stable.
        filter_file(
            'default = ["all", "nightly"]',
            'default = ["all"]',
            "py-polars/Cargo.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import polars as pl; print(pl.__version__)")
