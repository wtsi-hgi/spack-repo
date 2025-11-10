# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPolars(PythonPackage):
    """Blazingly fast DataFrame library."""

    homepage = "https://www.pola.rs/"
    pypi = "polars/polars-0.20.5.tar.gz"

    license("MIT")

    version("1.25.2", sha256="c6bd9b1b17c86e49bcf8aac44d2238b77e414d7df890afc3924812a5c989a4fe")
    version("0.20.5", sha256="fa4abc22cee024b5872961ddcd8a13a0a76150df345e21ce4308c2b1a36b47aa")

    # pyproject.toml
    depends_on("py-maturin@1.3.2:", type="build")
    depends_on("cmake", type="build")

    # Build with stable Rust; recipe patches strip nightly-only features
    depends_on("rust", type="build")

    def patch(self):
        # Some upstream Cargo manifests enable the `nightly` feature on dependencies like
        # `hashbrown`, which fails to compile on stable rust. Strip the `nightly` token
        # from feature lists for affected versions.
        if self.spec.satisfies("@0.20.5") or self.spec.satisfies("@1.25.2"):
            import glob

            for cargo_toml in glob.glob("**/Cargo.toml", recursive=True):
                # Remove occurrences of the "nightly" feature in feature lists
                filter_file(',\s*"nightly"', "", cargo_toml, string=True)
                filter_file('"nightly",\s*', "", cargo_toml, string=True)
                filter_file('"nightly"', "", cargo_toml, string=True)
                # Avoid requiring git metadata during build
                filter_file(',\s*"build_info"', "", cargo_toml, string=True)
                filter_file('"build_info",\s*', "", cargo_toml, string=True)
                filter_file('"build_info"', "", cargo_toml, string=True)
                # Clean up potential trailing or duplicate commas left by removal
                filter_file('\[,\s*', "[", cargo_toml, string=True)
                filter_file(',\s*\]', "]", cargo_toml, string=True)
                filter_file(',\s*,', ",", cargo_toml, string=True)
                # Remove lines that contain only a comma
                filter_file(r'^[\t ]*,[\t ]*$', "", cargo_toml)

            # Also remove nightly-only crate attributes like `#![feature(...)]` in Rust sources
            for rs_file in glob.glob("**/*.rs", recursive=True):
                filter_file(r"^#!\[feature\([^\)]*\)\].*\n", "", rs_file)

            # Replace nightly-only Vec::into_raw_parts usage with a stable equivalent
            for df_rs in glob.glob("**/py-polars/src/dataframe.rs", recursive=True):
                # Make 'cols' binding mutable (literal match)
                filter_file(
                    "let cols = unsafe { std::mem::take(df.get_columns_mut()) };",
                    "let mut cols = unsafe { std::mem::take(df.get_columns_mut()) };",
                    df_rs,
                    string=True,
                )
                # Replace into_raw_parts with manual pointer/len/cap extraction (literal match)
                filter_file(
                    "let (ptr, len, cap) = cols.into_raw_parts();",
                    (
                        "let ptr = cols.as_mut_ptr();\n"
                        "        let len = cols.len();\n"
                        "        let cap = cols.capacity();\n"
                        "        std::mem::forget(cols);"
                    ),
                    df_rs,
                    string=True,
                )

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # polars provides a Python module; verify import succeeds
            python("-c", "import polars as pl; print(pl.__version__)")
