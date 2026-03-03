# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCsbdeep(PythonPackage):
    """This is the CSBDeep Python package, which provides a toolbox for content-aware restoration of fluorescence microscopy images (CARE), based on deep learning via Keras and TensorFlow."""

    url = "https://github.com/CSBDeep/CSBDeep/archive/refs/tags/0.7.4.tar.gz"

    version("0.7.4", sha256="c16bd354fddd83fc301a9d75eb9b30eb3c14cf7f1b1a8a8166ee3bcee23ca4da")
    version("0.7.3", sha256="06f1276129de3387910c8d19cc3a3b0a0c2244e06958d36efb3e2af97e30a367")
    version("0.7.2", sha256="3cb56b54b76b20390fb01abdd01a84833d98a82816de28c56a94210372baca36")
    version("0.7.1", sha256="0de5d0a42d175e5e1d07ae51cd843f2f9c49310ade631c0490902460513e348c")
    version("0.7.0", sha256="567206c1b479cfde116d45cb833be10ce37bf8d7627ede1279cde0090917eebc")
    version("0.6.3", sha256="823b6569b5694c978898fa9acd2e3ed16655c71f304bbb83b8b94b64fa29c689")
    version("0.6.2", sha256="ba38a4a93834ae544ee687cb583950843bd01fb86a2f4a90c244b658ad2e6692")
    version("0.6.1", sha256="baf5a72cb7d2ff1cf6227f4cb9d6367fa9a264cb3bb960445476715c2303adfe")
    version("0.6.0", sha256="e29687da70d33f191075886e7970a5132f0dcff159d4fcdd8bc3a1a4896f909c")
    version("0.5.2", sha256="0cfa0c8d12a0411bc07b56844df3d7fa6d202cda39187b4e30127dce88f6b6a1")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
    depends_on("py-tifffile", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
