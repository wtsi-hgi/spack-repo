# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""
Example rationale: Demonstrates non-C toolchains (Rust/LLVM) as build dependencies.

What this teaches:
- Set pypi to the source tarball path and declare version() with sha256.
- Prefer sha256 over md5 for modern sources.
- Use depends_on("pkg", type=("build", "run")) to scope dependency roles.
- Include non-C toolchains (rust/llvm) when upstream uses them.
"""
from spack.package import *

class PyDeltalake(PythonPackage):
    """Native Delta Lake Python binding based on delta-rs with Pandas integration."""

    homepage = "https://github.com/delta-io/delta-rs"
    pypi = "deltalake/deltalake-0.15.3.tar.gz"

    version("0.15.3", sha256="c24ad4644b92d65dccf132b48c73e61bc07416b7a8b69e345c7f437217c44b2b")

    depends_on("rust@1.73.0:", type="build")
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-maturin", type=("build"))
