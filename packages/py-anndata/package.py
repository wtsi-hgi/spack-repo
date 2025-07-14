# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAnndata(PythonPackage):
    """anndata is a Python package for handling annotated data matrices in memory and on disk, positioned between pandas and xarray. anndata offers a broad range of computationally efficient features including, among others, sparse data support, lazy operations, and a PyTorch interface."""

    homepage = "https://github.com/scverse/anndata"
    pypi = "anndata/anndata-0.10.3.tar.gz"

    version("0.11.1", sha256="36bff9a85276fc5f1b9fd01f15aff9aa49408129985f42e0fca4e2c5b7fa909f")
    version("0.10.3", sha256="3a40eb6a30e976a3f2678a09e89cd8819bb19b3944278b94eb2d568060d30344")
    version("0.9.2", sha256="e5b8383d09723af674cae7ad0c2ef53eb1f8c73949b7f4c182a6e30f42196327")
    version("0.8.0", sha256="94d2cc6f76c0317c0ac28564e3092b313b7ad19c737d66701961f3e620b9066e")
    version("0.7.8", sha256="1efd7eb40839e0325bb066238280228a980d7dde6410793dbff2835f44a2d3ef")
    version("0.7.7", sha256="f7a7734d217c5cc80c7964ba42be87a58c3f1113ac4dd947a4ae9bf49097cccb")
    version("0.7.6", sha256="a3cc67bba9a4cd4b5984aec64c4f577c2d5a4695f4064027f8e6a9dac1f508b2")
    version("0.7.5", sha256="2113a7463388013023f153e1a1446add4182883e3320b6e37dda18ee6210e038")
    version("0.7.4", sha256="da1c3a3ad8729907874fb464d4a22bab8d86d732e35d18adbfdfd8474fc75edb")

    depends_on("py-hatchling", type=("build", "run"))
    depends_on("py-hatch-vcs", type=("build", "run"))
    # https://github.com/scverse/anndata/issues/1210
    depends_on("py-pandas@:2.1.1,2.1.3:", type=("build", "run"))  # skip 2.1.2
    depends_on("py-pytoml", type=("build", "run"), when="@:0.7.8")
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))

    with when("@:0.9"):
        depends_on("py-flit-core", type="build")

    with when("@0.10:"):
        depends_on("python@3.11:", type=("build", "run"))

