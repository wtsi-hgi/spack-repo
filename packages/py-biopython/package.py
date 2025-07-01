# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBiopython(PythonPackage):
    """A distributed collaborative effort to develop Python libraries and
    applications which address the needs of current and future work in
    bioinformatics.
    """

    homepage = "https://biopython.org/wiki/Main_Page"
    pypi = "biopython/biopython-1.79.tar.gz"
    git = "https://github.com/biopython/biopython.git"

    maintainers("RMeli")

    license("BSD-3-Clause")

    version("1.85", sha256="5dafab74059de4e78f49f6b5684eddae6e7ce46f09cfa059c1d1339e8b1ea0a6", preferred=True)
    version("20241216", commit="19557112226370694e6f5a06214100f051f32125")
    version("1.81", sha256="2cf38112b6d8415ad39d6a611988cd11fb5f33eb09346666a87263beba9614e0")
    version("1.80", sha256="52805e9af88767e450e2df8113b5bc59e964e2e8a7bb803a83570bdbb51c0e43")
    version("1.79", sha256="edb07eac99d3b8abd7ba56ff4bedec9263f76dfc3c3f450e7d2e2bcdecf8559b")
    version("1.78", sha256="1ee0a0b6c2376680fea6642d5080baa419fd73df104a62d58a8baf7a8bbe4564")
    version("1.73", sha256="70c5cc27dc61c23d18bb33b6d38d70edc4b926033aea3b7434737c731c94a5e0")
    version("1.70", sha256="4a7c5298f03d1a45523f32bae1fffcff323ea9dce007fb1241af092f5ab2e45b")
    version("1.65", sha256="6d591523ba4d07a505978f6e1d7fac57e335d6d62fb5b0bcb8c40bdde5c8998e")

    depends_on("python@2.6:2.7,3.3:3.9", type=("build", "run"), when="@1.63:1.68")
    depends_on("python@2.7,3.3:3.9", type=("build", "run"), when="@1.69")
    depends_on("python@2.7,3.4:3.9", type=("build", "run"), when="@1.70:1.74")
    depends_on("python@2.7,3.5:3.9", type=("build", "run"), when="@1.75:1.76")
    depends_on("python@3.6:", type=("build", "run"), when="@1.77:")
    depends_on("python@3.10:", type=("build", "run"), when="@1.85:")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    with when("@1.73"):
        patch("fix_disordered_get_list.patch")
