# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPolars(PythonPackage):
    """Lightning-fast DataFrame library for Rust and Python, powered by Apache Arrow."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-1.25.2.tar.gz"

    # Versions
    version("1.25.2", sha256="c6bd9b1b17c86e49bcf8aac44d2238b77e414d7df890afc3924812a5c989a4fe")

    # Python and build dependencies
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    # Build via maturin (Rust-based Python packaging)
    depends_on("py-maturin@1:", type="build")
    # Newer polars and transitive crates (e.g., home>=0.5.12) require newer rustc
    depends_on("rust@1.88:", type="build")

    # Ensure the rust toolchain used by maturin is discoverable
    def setup_build_environment(self, env):
        rust_bin = self.spec["rust"].prefix.bin
        env.prepend_path("PATH", rust_bin)

    # polars' Cargo.toml enables the "nightly" feature by default, which pulls
    # in unstable Rust features (failing on stable toolchains). Disable it.
    @when("@1.25.2")
    def patch(self):
        # Remove `nightly` from the default feature set in py-polars/Cargo.toml
        filter_file(
            'default = ["all", "nightly"]',
            'default = ["all"]',
            "py-polars/Cargo.toml",
            string=True,
        )

    @run_after("install")
    def install_test(self):
        # Prefer CLI test if available; fall back to Python import
        with working_dir("spack-test", create=True):
            python("-c", "import polars; print(polars.__version__)")
