# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAnndata(PythonPackage):
    """anndata is a Python package for handling annotated data matrices in memory and on disk, positioned between pandas and xarray. anndata offers a broad range of computationally efficient features including, among others, sparse data support, lazy operations, and a PyTorch interface."""

    homepage = "https://github.com/scverse/anndata"
    pypi = "anndata/anndata-0.10.3.tar.gz"

    version("0.10.3", sha256="3a40eb6a30e976a3f2678a09e89cd8819bb19b3944278b94eb2d568060d30344")
    version("0.9.2", sha256="e5b8383d09723af674cae7ad0c2ef53eb1f8c73949b7f4c182a6e30f42196327")

    depends_on("py-hatchling", type=("build", "run"))
    depends_on("py-hatch-vcs", type=("build", "run"))

    with when("@:0.9"):
        depends_on("py-flit-core", type="build")

    with when("@0.10:"):
        depends_on("python@3.11:", type=("build", "run"))
        depends_on("py-h5py", type=("build", "run"))
        depends_on("py-pandas", type=("build", "run"))
        depends_on("py-scipy", type=("build", "run"))
        depends_on("py-natsort", type=("build", "run"))
